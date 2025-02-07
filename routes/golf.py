from fastapi import APIRouter, Depends
from database import supabase

router = APIRouter(
    prefix="/golf",  # 🔹 모든 라우트가 `/golf` 경로를 사용하도록 설정
    tags=["golf"],  # 🔹 API 문서에서 'golf' 그룹으로 표시
)

# 1️⃣ 모든 골프장 가져오기
@router.get("/")
def get_all_golf_courses():
    response = supabase.table("golf_courses").select("*").execute()
    return response.data if response.data else []

# 2️⃣ 특정 골프장 가져오기
@router.get("/{golf_id}")
def get_golf_course(golf_id: int):
    response = supabase.table("golf_courses").select("*").eq("id", golf_id).execute()
    return response.data[0] if response.data else {"error": "Golf course not found"}

# 3️⃣ 새로운 골프장 추가하기
@router.post("/")
def add_golf_course(data: dict):
    response = supabase.table("golf_courses").insert(data).execute()
    return response.data

# 4️⃣ 기존 골프장 정보 수정
@router.put("/{golf_id}")
def update_golf_course(golf_id: int, data: dict):
    response = supabase.table("golf_courses").update(data).eq("id", golf_id).execute()
    return response.data

# 5️⃣ 골프장 삭제
@router.delete("/{golf_id}")
def delete_golf_course(golf_id: int):
    response = supabase.table("golf_courses").delete().eq("id", golf_id).execute()
    return {"message": "Golf course deleted"} if response.data else {"error": "Golf course not found"}