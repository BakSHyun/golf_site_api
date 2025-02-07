from fastapi import FastAPI
from routes import golf  # ⬅️ golf API 라우터 불러오기
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS 설정을 확실하게 적용
origins = [
    "http://golf-site-ten.vercel.app",  # Vercel 프론트엔드
    "https://golf-site-ten.vercel.app",  # Vercel 프론트엔드
    "https://golf-site.up.railway.app",  # Railway 백엔드
    "http://localhost:3000",  # 개발용
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ⭐ 특정 도메인 허용
    allow_credentials=True,
    allow_methods=["*"],  # ⭐ 모든 HTTP 메서드 허용 (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # ⭐ 모든 헤더 허용
    expose_headers=["*"],  # ⭐ 응답 헤더 공개 (CORS 적용)
)

# ✅ golf API 라우터 추가 (이 부분이 없으면 API가 사라짐)
app.include_router(golf.router)
# ✅ OPTIONS 요청 직접 처리 (CORS 문제 해결)
@app.options("/{full_path:path}")
async def preflight_handler():
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization",
    }
    return JSONResponse(content={}, headers=headers)
@app.get("/")
def home():
    return {"message": "Welcome to Golf API!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)