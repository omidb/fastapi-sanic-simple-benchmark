from fastapi import FastAPI
from .share import User, Address
from .user_service import UserService



app = FastAPI(title='api', debug=True)
user_service = UserService()

@app.post("/user/", response_model=Address)
async def create_user(user: User):
    address = user_service.create_address(user)
    return address

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8065)