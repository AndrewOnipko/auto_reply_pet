import json
from models.review import Question
from core.interfaces import ReviewProvider
from config import QUESTIONS_PATH
from core.logger import simple_logger

class FileReviewProvider(ReviewProvider):
    def __init__(self, logger):
        self.logger = logger

    @simple_logger
    async def get_questions(self, is_answered: bool = False, limit: int = 100, skip: int = 0):
        try:
            with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
                raw_data = json.load(f)

            questions = [Question(**item) for item in raw_data]

            if is_answered:
                return [q for q in questions if q.answer is not None]
            else:
                return [q for q in questions if q.answer is None]
        except Exception as e:
            self.logger.error(f"Ошибка при получении вопросов: {e}")
            return []