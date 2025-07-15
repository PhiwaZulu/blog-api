from fastapi import Request
from fastapi.responses import JSONResponse

async def content_type_middleware(request: Request, call_next):
    if request.method == "POST" and request.url.path.startswith("/posts"):
        if request.headers.get("content-type") != "application/json":
            return JSONResponse(status_code=415, content={"error": "Unsupported Media Type"})
    return await call_next(request)

async def payload_size_limit_middleware(request: Request, call_next):
    if request.method == "POST" and request.url.path == "/posts":
        body = await request.body()
        if len(body) > 10 * 1024 * 1024:  # 10MB
            return JSONResponse(status_code=413, content={"error": "Payload too large"})
    return await call_next(request)
