from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def authenticate():
    """
    Default route for authenticating.
    """
    return {"message": "Authenticated!"}