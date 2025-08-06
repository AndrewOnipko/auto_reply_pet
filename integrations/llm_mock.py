from core.interfaces import LLMClient
from core.logger import simple_logger


class MockLLMClient(LLMClient):
    def __init__(self, logger):
        self.logger = logger


    @simple_logger
    def generate_answer(self, question: str, product_name: str) -> str:
        if question == "Не нравится":
            return f"Понимаем, что {product_name} может не подойти. Какой товар вас интересует?"
        elif question == "Нравится":
            return f"Спасибо за вопрос! {product_name} — отличный выбор. Мы скоро дополним описание."
        else:
            return f"Спасибо за вопрос о товаре {product_name}. Мы свяжемся с вами при необходимости!"