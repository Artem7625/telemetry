import json
import redis  # type: ignore


# r = redis.Redis(host="localhost", port=6379, db=4)
r = redis.Redis(host="localhost", port=6379, db=4)


def get_service_data():
    """Gets service data from Redis database"""

    service_data = {}

    vehicle_model = r.get("vehicle:model")
    license_plate = r.get("vehicle:license_plate")
    engineer_full_name = r.get("comissioning:engineer")
    equipment = r.lrange("comissioning:history:2021-08-12:equipment", 0, -1)
    timestamp = r.get("comissioning:timestamp")

    service_data["vehicle_model"] = vehicle_model.decode("utf-8")
    service_data["license_plate"] = license_plate.decode("utf-8")
    service_data["name"] = engineer_full_name.decode("utf-8")
    service_data["equipment"] = [eq.decode("utf-8") for eq in equipment]
    service_data["timestamp"] = timestamp.decode("utf-8")

    return service_data


def set_engineer_name(name: str):
    r.set("comissioning:engineer", name)


def db_dump():
    dump_data = r.dump('comissioning:engineer')

    # Преобразование бинарных данных в JSON-совместимый формат
    def serialize_data(data):
        if data is None:
            return None
        return repr(data)

    json_dump = json.dumps({
        'key_name': serialize_data(dump_data),
    })

    # Сохранение дампа в JSON-файл
    with open('redis_dump.json', 'w') as json_file:
        json_file.write(json_dump)