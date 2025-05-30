from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import EmailStr, BaseModel

import uvicorn

from core.config import settings
from api_v1 import router as router_v1
from items_views import router as items_router
from users.views import router as users_router


@asynccontextmanager
async def lifespan(application: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def hello_index():
    return {"message": "Salam aleikum bro!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
