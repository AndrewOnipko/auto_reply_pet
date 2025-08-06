from abc import ABC, abstractmethod
from typing import List, Dict
from models.review import Question

class ReviewProvider(ABC):
    @abstractmethod
    async def get_questions(self, is_answered: bool = False, limit: int = 100, skip: int = 0) -> List[Question]:
        """Получает вопрос из мока вб."""

        pass


class LLMClient(ABC):
    @abstractmethod
    async def generate_answer(self, question: str, product_name: str) -> str:
        """Генерирует ответ в зависимости от вопроса."""

        pass


class ReplySender(ABC):
    @abstractmethod
    async def send_reply(self, replies: Dict[str, str]) -> None:
        """Принимает словарь, где ключ — ID вопроса, значение — сгенерированный ответ."""

        pass