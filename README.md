# Simple Blog API

This is a FastAPI-based Simple Blog API implementing the following functionality:
- GET all posts
- GET a single post by ID
- POST a new blog post with validation
- Custom error handlers and middleware

### 🚀 Running the App

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
