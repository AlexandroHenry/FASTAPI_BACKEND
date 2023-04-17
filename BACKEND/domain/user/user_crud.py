from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from passlib.context import CryptContext
import re
from fastapi import APIRouter, HTTPException, status

# MongoDB의 URL
MONGODB_URL = "mongodb://localhost:27017"

# AsyncIOMotorClient 객체 생성
client = AsyncIOMotorClient(MONGODB_URL)
db = client["test_db"]
user_collection = db["users"]

# 비밀번호 암호화를 위한 CryptContext 객체 생성
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_user_by_email(email: str):
    user = await user_collection.find_one({"email": email})
    return user

# 사용자 생성 (회원가입)
async def create_user(user_data: dict):
    # 비밀번호 암호화
    hashed_password = hash_password(user_data["password"])
    user_data["password"] = hashed_password

    # MongoDB에 사용자 데이터 저장
    result = await user_collection.insert_one(user_data)
    return result.inserted_id

# 비밀번호 암호화 함수
def hash_password(password: str) -> str:
    # 비밀번호에 대한 검증 조건 설정
    if len(password) < 8 or len(password) > 15:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="비밀번호는 8~15자리여야 합니다.")
    if not re.search(r"\d", password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="비밀번호는 숫자가 하나 이상 포함되어야 합니다.")
    if not re.search(r"[!@#$%^&*]", password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="비밀번호는 특수문자가 하나 이상 포함되어야 합니다.")
    return pwd_context.hash(password)