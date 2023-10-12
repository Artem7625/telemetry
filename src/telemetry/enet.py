import asyncio

from modules.enet_wrapper import EnetClient, AgroProto, Data, get_property_name
from agroproto.data.ImageFormat import ImageFormat


class EnetHandler:
    """Класс взаимодействия с Enet-сервером."""

    def __init__(self):
        self.enet_client = EnetClient()

    async def connect(self, host, port):
        """Подключается к Enet-серверу."""
        return await asyncio.to_thread(self.enet_client.connect, host, port)

    async def disconnect(self):
        """Разрывает соединение с Enet-сервером."""
        await asyncio.to_thread(self.enet_client.disconnect)

    async def receive_data(self):
        """Асинхронно получает данные с Enet-сервера."""

        message = await asyncio.to_thread(self.enet_client.receive_message)
        if message is not None:
            parsed_data = AgroProto.parse_message(message)
            return parsed_data
        return None

    async def process_data(self, parsed_data):
        """Асинхронно обрабатывает данные, полученные с Enet-сервера."""

        if parsed_data is not None:
            if parsed_data.type == Data.CommonInfo:
                return self.process_common_info(parsed_data.data)
            elif parsed_data.type == Data.View:
                return self.process_view(parsed_data.data)
        return None

    def process_common_info(self, data):
        """Обрабатывает данные об общей информации."""

        return {
            "cte": data.cte,
            "speed": data.speed,
        }

    def process_view(self, data):
        """Обрабатывает данные изображения."""

        image = data.image
        image_format = get_property_name(ImageFormat, image.format)
        if image_format == "Jpeg":
            return bytes(image.data)
