from typing import Annotated
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Security
from fastapi.security import APIKeyHeader
import jwt
from .utils import check_expiry
from .database import User

# Secret key for encoding and decoding JWT tokens (this should be kept secret in a real application)
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"  # Algorithm for encoding JWT tokens

# Define the token header
token = APIKeyHeader(
    name="Authorization",
    scheme_name="Authorization Header",
    description="Add the **access Token** and explore the rest of the api.",
    auto_error=False,
)

# Function to generate a JWT token
def generate_token(email: str):
    expiration_time = datetime.utcnow() + timedelta(hours=1)  # Token expiration time (1 hour)
    payload = {"email": email, "exp": expiration_time}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(auth_token: Annotated[str, Security(token)]):
    if auth_token is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": "Authorization Header Not found",
                "help": "Add Authorization Header with an Valid Token",
            },
            headers={"Authorization": "Bearer Token"},
        )
    if "Bearer" not in auth_token:
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            detail={"message": "Bearer is Missing from Authorization Header Value"},
            headers={"Authorization": "Bearer Token"},
        )

    try:
        decoded_jwt = jwt.decode(auth_token.split(" ")[1], SECRET_KEY, algorithms=[ALGORITHM])
        expiry_date = decoded_jwt.get("exp")
        if not check_expiry(expiry_date):
            raise HTTPException(
                status.HTTP_403_FORBIDDEN,
                detail={
                    "message": "Token Expired",
                    "help": "Login Again to generate a new Token.",
                },
            )
        user_data = User.objects(email=decoded_jwt.get("email")).first()
        if user_data is None:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND, detail="Unauthorized Access"
            )
        return (user_data.email, user_data.is_verified, user_data.id)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            detail={"message": "Token Expired", "help": "Login Again to generate a new Token."},
        )
    except (jwt.DecodeError, IndexError):
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, detail="Invalid Token")
