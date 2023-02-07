from typing import Dict, List, Optional
from fastapi import APIRouter, Query ,Body,Path
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
  title: str
  content: str
  nb_comments: int
  published: Optional[bool]
  tags: List[str] = []
  metadata: Dict[str, str] = {'key1': 'val1'}
  image: Optional[Image] = None

@router.post('/new')
# ได้แปลงจาก JSON เป็นโมเดลและได้ส่งข้อมูลนั้นไปยังฟังก์ชัน
def create_blog(blog: BlogModel, id: int, version: int = 1):
  return {
    'id': id,
    'data': blog,
    'version': version
    }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int, 
        comment_title: str = Query(None,
            title='ชื่อเรื่อง comment',
            description='คำอธิบายบางอย่างสำหรับ comment_title',
            alias='commentTitle',
            deprecated=True
        ),
        content: str = Body(...,
            min_length=10,
            max_length=50,
            regex='[ก-๏\s]+$'#กำหนดรูปแบบข้อความ
            #regex='^[a-z\s]*$'
        ),
        v: Optional[List[str]] = Query(['1.0', '1.1', '1.2']),
        comment_id: int = Path(None, le=50)
    ):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'version': v,
        'comment_id': comment_id
    }

def required_functionality():
  return {'message': 'การเรียนรู้ FastAPI เป็นสิ่งสำคัญ'}