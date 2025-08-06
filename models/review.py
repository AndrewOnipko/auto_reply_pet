# models/review.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ProductDetails(BaseModel):
    imtId: int
    nmId: int
    productName: str
    supplierArticle: str
    supplierName: str
    brandName: str


class Question(BaseModel):
    id: str
    text: str
    createdDate: datetime
    state: str
    answer: Optional[dict]
    productDetails: ProductDetails
    wasViewed: bool
    isWarned: bool