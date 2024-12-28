from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from core.security import create_access_token, verify_password
from db.database import get_db
from db.models import User
from schemas.schemas import UserLogin, Token

router = APIRouter()

@router.post("", response_model=Token, tags=["Authentication"])
def login(
    login_data: UserLogin,
    db: Session = Depends(get_db)
):
    
    user = db.query(User).filter(User.email == login_data.email).first()
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "Bearer"}
