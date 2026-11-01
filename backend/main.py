from fastapi import FastAPI
from routers import booking

app = FastAPI(title="LifeLine Backend", version="1.0")

# Bookings router ko include karna
app.include_router(booking.router)

@app.get("/")
def read_root():
    return {"message": "LifeLine Emergency API is running successfully!"}