from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password : str):
    return pwd_context.hash(password)

def verify(plain_passwd : str, hashed_passwd : str):
    return pwd_context.verify(plain_passwd,hashed_passwd)