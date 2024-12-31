from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "John Doe"
    # signup_ts: datetime | None = None
    # friends: list[int] = []


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str

# Sanic
# http.response_time:
#   min: ......................................................................... 0
#   max: ......................................................................... 5
#   mean: ........................................................................ 0.4
#   median: ...................................................................... 0
#   p95: ......................................................................... 1
#   p99: ......................................................................... 2

#Fast API
