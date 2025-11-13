from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Privacy Policy API",
    version="v1.0.0",
    description="Returns the public privacy policy link for GPT integrations."
)

@app.get("/privacy-policy")
def get_privacy_policy():
    return JSONResponse(
        content={
            "url": "https://docs.google.com/document/d/e/2PACX-1vRrKPRw--8yN7v3J6lIEBdkw9uEMEQTZRDOQtMVFgfd85zMC_c8wui0yes9GUO7RYFU6Q1MHPe4LaA3/pub"
        }
    )
