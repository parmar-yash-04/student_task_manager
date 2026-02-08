from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse
from app.utils import hash_password
from app import oauth2 

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/create", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    hashed_password = hash_password(user.password)
    new_user = User(
        email=user.email,
        username=user.username,
        full_name=user.full_name,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# @router.get("/", response_model=list[UserResponse])
# def get_all_users(db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
#     users = db.query(User).all()
#     return users

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if current_user.id != user_id:
        raise HTTPException(
            status_code=403,
            detail="you can't delete this user"
        )
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}