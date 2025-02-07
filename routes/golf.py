from fastapi import APIRouter
from database import supabase

router = APIRouter()

# 1️⃣ 모든 골프장 가져오기
@router.get("/golf")
def get_all_golf_courses():
    response = supabase.table("golf_courses").select("*").execute()
    
    # 🔹 만약 데이터가 없으면 빈 배열([]) 반환
    return response.data if response.data else []

# 2️⃣ 특정 골프장 가져오기
@router.get("/golf/{golf_id}")
def get_golf_course(golf_id: int):
    response = supabase.table("golf_courses").select("*").eq("id", golf_id).execute()
    return response.data[0] if response.data else {"error": "Golf course not found"}

# 3️⃣ 새로운 골프장 추가하기
@router.post("/golf")
def add_golf_course(data: dict):
    response = supabase.table("golf_courses").insert(data).execute()
    return response.data

# 4️⃣ 기존 골프장 정보 수정
@router.put("/golf/{golf_id}")
def update_golf_course(golf_id: int, data: dict):
    response = supabase.table("golf_courses").update(data).eq("id", golf_id).execute()
    return response.data

# 5️⃣ 골프장 삭제
@router.delete("/golf/{golf_id}")
def delete_golf_course(golf_id: int):
    response = supabase.table("golf_courses").delete().eq("id", golf_id).execute()
    return {"message": "Golf course deleted"} if response.data else {"error": "Golf course not found"}