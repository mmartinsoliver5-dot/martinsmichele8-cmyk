from fastapi import FastAPI
from app.routers import meters, readings, photos, anomalies, reports

app = FastAPI(title="IoT Hidrômetros API")

app.include_router(meters.router)
app.include_router(readings.router)
app.include_router(photos.router)
app.include_router(anomalies.router)
app.include_router(reports.router)


@app.get("/health")
async def health():
    return {"status": "ok"}
