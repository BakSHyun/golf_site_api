from fastapi import FastAPI
from routes import golf  # ⬅️ golf API 라우터 불러오기
# ✅ CORS 설정 추가 (이전 오류 해결 코드)
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    redirect_slashes=False  # ✅ /golf → /golf/ 자동 리디렉트 활성화
)
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

# ✅ golf API 라우터 추가 (이 부분이 없으면 API가 사라짐)
app.include_router(golf.router)

@app.get("/")
def home():
    return {"message": "Welcome to Golf API!"}