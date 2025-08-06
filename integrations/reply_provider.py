from core.interfaces import ReplySender
from core.logger import simple_logger
from typing import Dict

class MockReplySender(ReplySender):
    def __init__(self, logger):
        self.logger = logger


    @simple_logger
    async def send_reply(self, replies: Dict[str, tuple[str, str]]) -> None:
        from asyncio import sleep
        await sleep(0.1)

        for question_id, (question_text, answer) in replies.items():
            print(f"\nВопрос (ID: {question_id}):\n{question_text}\n\nОтвет:\n{answer}\n")
