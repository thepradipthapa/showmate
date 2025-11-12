from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.status import HTTP_200_OK

app = FastAPI(title="ShowMate API", version="1.0.0")


@app.get("/", response_class=JSONResponse)
def root():
    return JSONResponse(
        content={"message": "🎬 Welcome to ShowMate API!", "status": "running"},
        status_code=HTTP_200_OK
    )
