from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine, Base
from routers import login, signup
from core.config import DATABASE_URL

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router, prefix="/login", tags=["Login"])
app.include_router(signup.router, prefix="/signup", tags=["Signup"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Bulletin Board API"}
