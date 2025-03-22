from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from dotenv import load_dotenv
import os
from .database import SessionLocal


load_dotenv()

SECRET_KEY = os.getenv ('AUTH_SECERET_KEY')
ALGORITHM = os.getenv('AUTH_ALGORITHM')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        db_dependency = Annotated[Session, Depends(get_db)]

        bcrypt_context = CryptContext(schemes=["bcrypt"], deprecenated="auto")
        oauth2_scheme = OAuth2PasswordBearer(tokenUrl='aut/token')
        oauth2_bearer_dependency = Annotated[str, Depends(oauth2_bearer)]


    async def get_current_user(token, SECRET_KEY, algorithms=[ALGORITHM]):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms= [ALGORITHM])
            username: str = payload.get('sub')
            user_id: int = payload.get('user_id')
            if username is None or user_id is None:
                raise HTTPException(status_code=HTTPException.status_code_401_UNAUTHORIZED, detail='Could not validate credentials')
            return {'username': username, 'user_id': user_id}
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
        
        user_dependency = Annotated[dict, Depends(get_current_user)]
                
        