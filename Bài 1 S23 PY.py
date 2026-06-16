import math
import os
from datetime import datetime, timedelta


shipments = [
    {
        "id": "TRK-001",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 10.8231,
        "to_lon": 106.6297,
        "depart": "2026-06-10 08:00:00",
        "deadline": "2026-06-11 12:00:00"
    },
    {
        "id": "TRK-002",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 16.0544,
        "to_lon": 108.2022,
        "depart": "2026-06-10 09:30:00",
        "deadline": "2026-06-10 15:00:00"
    }
]


def create_log_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def calculate_distance(lat1, lon1, lat2, lon2):
    radius = 6371

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)

    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return radius * c


def predict_eta(departure_str, distance_km, speed=60):
    departure_time = datetime.strptime(
        departure_str,
        "%Y-%m-%d %H:%M:%S"
    )

    hours_needed = distance_km / speed

    eta = departure_time + timedelta(
        hours=hours_needed
    )

    return eta


print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")

create_log_dir("logs")

print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
print("-" * 75)

for shipment in shipments:

    distance = calculate_distance(
        shipment["from_lat"],
        shipment["from_lon"],
        shipment["to_lat"],
        shipment["to_lon"]
    )

    eta = predict_eta(
        shipment["depart"],
        distance
    )

    deadline = datetime.strptime(
        shipment["deadline"],
        "%Y-%m-%d %H:%M:%S"
    )

    print(f"[CHUYẾN XE {shipment['id']}]")
    print(f" + Khoảng cách vận chuyển: {distance:.2f} km")
    print(f" + Thời gian khởi hành: {shipment['depart']}")
    print(f" + Dự kiến cập bến (ETA): {eta}")

    if eta <= deadline:
        print(" + Trạng thái:  AN TOÀN (Kịp tiến độ trước deadline)")
    else:
        print(
            f" + Trạng thái:  CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc "
            f"{deadline.strftime('%H:%M:%S')})"
        )

    print()

print("=" * 56)