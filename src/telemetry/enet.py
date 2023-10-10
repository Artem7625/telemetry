from modules.enet_wrapper import EnetClient, AgroProto, Data, get_property_name
from agroproto.data.ImageFormat import ImageFormat


class EnetHandler:
    def __init__(self):
        self.enet_client = EnetClient()

    def connect(self, host, port):
        return self.enet_client.connect(host, port)

    def receive_data(self):
        message = self.enet_client.receive_message()
        if message is not None:
            parsed_data = AgroProto.parse_message(message)
            return parsed_data
        return None

    def process_data(self, parsed_data):
        if parsed_data is not None:
            if parsed_data.type == Data.CommonInfo:
                return self.process_common_info(parsed_data.data)
            elif parsed_data.type == Data.View:
                return self.process_view(parsed_data.data)
        return None

    def process_common_info(self, data):
        return {
            "cte": data.cte,
            "speed": data.speed
        }

    def process_view(self, data):
        image = data.image
        image_format = get_property_name(ImageFormat, image.format)
        if image_format == "Jpeg":
            return bytes(image.data)
