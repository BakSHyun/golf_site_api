from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware
from routes.golf import router as golf_router

app = FastAPI()

# ✅ CORS 설정 (Vercel & 로컬 개발 허용)
origins = [
    "https://golf-site-ten.vercel.app",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ CORS 응답을 강제 적용하는 미들웨어
class ForceCORSHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        origin = request.headers.get("Origin", "")

        if origin in origins:  # ✅ 요청한 Origin이 허용된 목록에 있으면 헤더 추가
            response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        return response

app.add_middleware(ForceCORSHeadersMiddleware)  # ✅ 미들웨어 실행 순서 확인

# ✅ CORS 설정 이후에 라우트 추가
app.include_router(golf_router)


@app.get("/")
def home():
    return {"message": "Welcome to Golf API!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)