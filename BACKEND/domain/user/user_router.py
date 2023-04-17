from fastapi import APIRouter, HTTPException, status
from .user_schema import User
from .user_crud import create_user, get_user_by_email
from datetime import datetime
import uuid

router = APIRouter(
    prefix="/api/v1/users",
)

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: User):
    # 이메일 중복 확인
    existing_user = await get_user_by_email(user.email)
    
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="해당 이메일로 이미 회원 가입이 되어있습니다.")

    # 사용자 정보 저장
    user_data = {
        "email": user.email,
        "password": user.password,
        "username": user.username,
        "firstname": user.firstname,
        "lastname": user.lastname,
        "gender": user.gender,
        "nationality": user.nationality,
        "dob": user.dob,
        "createdAt": datetime.now(),
        "updatedAt": datetime.now(),
        "profileimg": user.profileimg,
        "role": "user"
    }

    result = await create_user(user_data)

    # 저장한 사용자 정보 반환
    return {"user_id": str(result)}




