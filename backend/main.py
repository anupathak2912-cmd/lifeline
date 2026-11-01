from fastapi import FastAPI
from routers import booking

app = FastAPI(title="LifeLine Backend", version="1.0")
from fastapi.middleware.cors import CORSMiddleware

# CORS configuration to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app.include_router(booking.router)

@app.get("/")
def read_root():
    return {"message": "LifeLine Emergency API is running successfully!"}