from core.interfaces import ReviewProvider
from models.review import Question, ProductDetails
from datetime import datetime
from core.logger import simple_logger

class MockWbAnswerProvider(ReviewProvider):
    def __init__(self, logger):
        self.logger = logger


    @simple_logger
    def get_questions(self, is_answered: bool = False, limit: int = 100, skip: int = 0):
        
        question_one = Question(
            id="some_id_1",
            text="Не нравится",
            createdDate = datetime.now(),
            state = "suppliersPortalSynch",
            answer = None,
            productDetails = ProductDetails(
                imtId=123,
                nmId=456,
                productName = "Coffee",
                supplierArticle = "123456",
                supplierName = "Coffee Shop",
                brandName= "Some Coffee Brand"
            ),
            wasViewed = False,
            isWarned = False
        )

        question_two = Question(
            id="some_id_2",
            text="something text",
            createdDate = datetime.now(),
            state = "wbRu",
            answer = {"text": "Спасибо за вопрос!"},
            productDetails = ProductDetails(
                imtId=12345,
                nmId=6789,
                productName = "Candy",
                supplierArticle = "123456",
                supplierName = "Candy Shop",
                brandName= "Some Candy Brand"
            ),
            wasViewed = False,
            isWarned = False
        )

        questions = [question_one, question_two]
        if is_answered:
            return [q for q in questions if q.answer is not None]
        else:
            return [q for q in questions if q.answer is None]


        