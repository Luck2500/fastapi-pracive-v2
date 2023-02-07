from router.blog_post import required_functionality
from fastapi import APIRouter,Response, status, Depends
from typing import Optional
from enum import Enum

router = APIRouter(
    prefix='/blog',#กำหนดคำนำหน้าของ path
    tags=['blog']  #กำหนดการดำเนินการที่มี tags ซึ่งเป็นการจัดหมวดหมู่ทั้งหมด
)

# @app.get('/blog/all')
# def get_all_blogs():
#   return {'message': 'All blogs provided'}

@router.get('/all',
        summary='ดึงข้อมูล blog ทั้งหมด',
        description='การเรียก API นี้เป็นการจำลองการดึงข้อมูล blog ทั้งหมด',
        response_description="รายการ blogs ที่มีอยู่"
        )
# ใช้ประเภทตัวเลือกเราจะระบุประเภทที่แท้จริงของพารามิเตอร์และเราสามารถระบุได้
def get_blogs(page = 1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
  return {'message': f'All {page_size} blogs on page {page}', 'req': req_parameter}

# การดำเนินการที่มี tags ซึ่งเป็นการจัดหมวดหมู่
@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
  """
    จำลองการดึง Comment ของ blog
    - **id** พารามิเตอร์เส้นทางบังคับ
    - **comment_id** พารามิเตอร์เส้นทางบังคับ
    - **bool** พารามิเตอร์ข้อความค้นหาที่ไม่บังคับ
    - **username** พารามิเตอร์ข้อความค้นหาที่ไม่บังคับ
    """
  return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/type/{type}')
def get_blog_type(type: BlogType):
  return {'message': f'Blog type {type}'}

@router.get('/{id}', status_code=status.HTTP_200_OK)
# สามารถตั้งค่าการตอบสนองนี้ที่ส่งโดยอัตโนมัติโดย Fast API ไปยังฟังก์ชัน
def get_blog(id: int, response: Response):
  if id > 5:
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': f'Blog {id} ไม่พบ'}
  else : 
    response.status_code = status.HTTP_200_OK
    return {'message': f'Blog มีรหัส {id}'}