from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware
from routes.golf import router as golf_router

app = FastAPI(
    redirect_slashes=False  # ✅ 자동 슬래시 리다이렉트 방지
)

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

# ✅ CORS 설정 이후에 라우트 추가해야 함
app.include_router(golf_router)  # 🚨 CORS 미들웨어보다 나중에 실행!


@app.get("/")
def home():
    return {"message": "Welcome to Golf API!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)