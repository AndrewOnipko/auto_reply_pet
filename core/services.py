from core.logger import simple_logger

class AutoReplyService:
    def __init__(self, review_provider, llm_client, reply_sender, logger):
        self.review_provider = review_provider
        self.llm_client = llm_client
        self.reply_sender = reply_sender
        self.logger = logger

    @simple_logger
    async def run(self):
        try:
            questions = await self.review_provider.get_questions(is_answered=False, limit=100, skip=0)
            generated_answers = {}
            for question in questions:
                answer = await self.llm_client.generate_answer(
                    question=question.text,
                    product_name=question.productDetails.productName
                )
                generated_answers[question.id] = (question.text, answer)
            await self.reply_sender.send_reply(generated_answers)
        except Exception as e:
            self.logger.error(f"Ошибка в AutoReplyService: {e}")
            raise e