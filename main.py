from fastapi import FastAPI
from routes import golf  # ⬅️ golf API 라우터 불러오기

app = FastAPI()

# ✅ CORS 설정 추가 (이전 오류 해결 코드)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Next.js 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ golf API 라우터 추가 (이 부분이 없으면 API가 사라짐)
app.include_router(golf.router)

@app.get("/")
def home():
    return {"message": "Welcome to Golf API!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)