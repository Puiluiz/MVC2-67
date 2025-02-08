import json
from collections import defaultdict

class DriverModel:
    def __init__(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    def get_all_drivers(self):
        return self.data

    def get_driver_counts(self):
        driver_counts = defaultdict(lambda: defaultdict(int))

        for driver in self.data:
            driver_type = driver["driver_type"]
            status = driver["license_status"]
            driver_counts[driver_type][status] += 1  # เพิ่มจำนวนผู้ขับขี่ตามประเภทและสถานะ

        return driver_counts