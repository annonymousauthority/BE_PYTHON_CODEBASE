from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


USERS = ["Paul", "Philip", "Simone", "Simon"]

@router.get("/getAllUsers")
async def get_all_users():
    try:
        return {"Users" : USERS}
    except Exception as e:
        raise e
    
@router.delete("/deleteuser/{user_name}")
async def delete_user(user_name: str):
    try:
        if user_name in USERS:
            USERS.remove(user_name)
            return {"Message": "User Deleted Successfully"}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class User(BaseModel):
    username: str

@router.post("/createuser")
async def create_user(user: User):
    try:
       if user.username in USERS:
           raise HTTPException(status_code=405, detail="User already exists")
       else:
           USERS.append(user.username)
           return {"Message":"User added successfully"} 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))