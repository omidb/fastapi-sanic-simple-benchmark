from sanic import Sanic, json
from sanic_ext import validate
from .share import User
from .user_service import UserService

app = Sanic("user_service")
user_service = UserService()

@app.post("/user/")
@validate(User)
async def create_user(request, body: User):
    address = user_service.create_address(body)
    return json(address.model_dump())

# if __name__ == "__main__":
#     app.run(host="localhost", port=8086, debug=True)