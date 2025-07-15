from fastapi import FastAPI
from app.routes import router as post_router
from app.middleware import payload_size_limit_middleware, content_type_middleware
from app.errors import validation_exception_handler, http_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException

app = FastAPI(title="Intelliscient  Blog API", version="1.0.0")

# Include routes
app.include_router(post_router)

# Register middleware
app.middleware("http")(payload_size_limit_middleware)
app.middleware("http")(content_type_middleware)

# Register custom error handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
