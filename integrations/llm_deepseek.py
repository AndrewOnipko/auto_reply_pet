from openai import AsyncOpenAI
from config import DEEPSEEK_API_KEY, DEEPSEEK_API_URL, LLM_PROMPT, AI_MODEL
from core.interfaces import LLMClient
from core.logger import simple_logger

class DeepSeekLLMClient(LLMClient):
    def __init__(self, logger):
        self.logger = logger
        self.client = AsyncOpenAI(
            api_key=DEEPSEEK_API_KEY,
            base_url=DEEPSEEK_API_URL + "/v1",
            default_headers={
                "HTTP-Referer": "http://localhost",
                "X-Title": "AutoReplyWB"
            }
        )


    @simple_logger
    async def generate_answer(self, question: str, product_name: str) -> str:
        prompt = f"{question}\nТовар: {product_name}"

        try:
            response = await self.client.chat.completions.create(
                model=AI_MODEL,
                messages=[
                    {"role": "system", "content": LLM_PROMPT},
                    {"role": "user", "content": prompt}],
                temperature=0.7)
            
            return response.choices[0].message.content
        except Exception as e:
            self.logger.error(f"Ошибка при обращении к DeepSeek через OpenRouter: {e}")
            return "Извините, мы не смогли обработать ваш вопрос."
