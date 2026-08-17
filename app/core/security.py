from datetime import datetime, timedelta, timezone
from jose import jwt # pyright: ignore[reportMissingModuleSource]
from passlib.context import CryptContext # pyright: ignore[reportMissingImports]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "sua_chave_secreta_super_mega_ultra_segura_mude_depois"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha de texto puro confere com o hash armazenado"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> bool:
    """Gera o hash segura de uma senha"""
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None=None):
    """Gera um tokem JWT com tempo de expiração"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt