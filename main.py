from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware
from routes.golf import router as golf_router

app = FastAPI()
app.include_router(golf_router)  # ✅ FastAPI의 기존 CORS 정책 유지
# ✅ 허용할 프론트엔드 도메인 설정
origins = [
    "https://golf-site-ten.vercel.app",  # Vercel (프론트엔드)
    "http://golf-site-ten.vercel.app",  # Vercel (프론트엔드)
    "https://golf-site-ten.vercel.app/",  # Vercel (프론트엔드)
    "https://golf-site.up.railway.app",  # Railway (백엔드)
    "http://localhost:3000",  # 로컬 개발 환경
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 특정 도메인만 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 요청 헤더 허용
)

# ✅ 모든 응답에 Access-Control-Allow-Origin을 강제로 추가하는 미들웨어
class AddCORSHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["Access-Control-Allow-Origin"] = request.headers.get("Origin", "https://golf-site-ten.vercel.app")
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        return response


app.add_middleware(AddCORSHeadersMiddleware)  # 🚨 **이제 CORSMiddleware보다 먼저 실행됨!**


@app.get("/")
def home():
    return {"message": "Welcome to Golf API!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)