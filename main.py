import logging
import os
import sys
import asyncio

from integrations.llm_deepseek import DeepSeekLLMClient
from integrations.reply_provider import MockReplySender
from integrations.file_review_provider import FileReviewProvider
from core.services import AutoReplyService
from controllers.main_controller import MainController

def setup_logging():
    script_path = os.path.abspath(sys.argv[0])
    file_directory = os.path.dirname(script_path)
    log_file = os.path.join(file_directory, 'logs.log')

    formatter = logging.Formatter('%(asctime)s - %(message)s')

    logging.basicConfig(level=logging.DEBUG,
                        handlers=[
                            logging.FileHandler(log_file, encoding='utf-8', mode='w'),
                            logging.StreamHandler()
                        ])
    for handler in logging.getLogger().handlers:
        handler.setFormatter(formatter)

async def main():
    try:
        logger = logging.getLogger()
        review_provider = FileReviewProvider(logger)
        llm_client = DeepSeekLLMClient(logger)
        reply_sender = MockReplySender(logger)
        auto_reply_service = AutoReplyService(review_provider, llm_client, reply_sender, logger)
        main_controller = MainController(auto_reply_service, logger)
        await main_controller.run()
    except Exception as e:
        logger.error(f"Ошибка в основном процессе: {e}")
        raise e

if __name__ == '__main__':
    setup_logging()
    asyncio.run(main())
