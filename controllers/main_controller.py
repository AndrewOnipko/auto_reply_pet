from core.logger import simple_logger

class MainController:
    def __init__(self, auto_reply_service, logger):
        self.auto_reply_service = auto_reply_service
        self.logger = logger


    @simple_logger
    async def run(self):
        await self.auto_reply_service.run()