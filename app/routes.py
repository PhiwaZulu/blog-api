from fastapi import APIRouter, HTTPException, Path, status
from datetime import datetime
from app.models import Post, PostBase

router = APIRouter()

# Simulated in-memory DB
posts_db = []
post_id_counter = 1

@router.get("/posts", response_model=list[Post])
async def get_all_posts():
    return posts_db

# Change path param to title: str instead of postId:int
@router.get("/posts/{title}", response_model=Post)
async def get_single_post(title: str = Path(..., min_length=1)):
    # Case-insensitive search (optional)
    post = next((p for p in posts_db if p["title"].lower() == title.lower()), None)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.post("/posts", response_model=Post, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase):
    global post_id_counter

    # Check for unique title
    if any(p["title"].lower() == post.title.lower() for p in posts_db):
        raise HTTPException(status_code=422, detail="Title must be unique")

    new_post = Post(
        id=post_id_counter,
        title=post.title,
        content=post.content,
        author=post.author or "Anonymous",
        createdAt=datetime.utcnow().isoformat() + "Z"
    )
    posts_db.append(new_post.dict())
    post_id_counter += 1
    return new_post

@router.api_route("/posts", methods=["PUT", "PATCH", "DELETE"])
@router.api_route("/posts/{title}", methods=["POST", "PUT", "PATCH", "DELETE"])
async def method_not_allowed():
    raise HTTPException(status_code=405, detail="Method not allowed")
