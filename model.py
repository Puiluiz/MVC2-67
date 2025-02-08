import json  # โมดูลสำหรับจัดการข้อมูลในรูปแบบ JSON
from collections import defaultdict  # ใช้ defaultdict เพื่อจัดการข้อมูลนับจำนวนได้สะดวก

class DriverModel:
    def __init__(self, json_file):
        # ตัวสร้าง (Constructor) สำหรับโหลดข้อมูลผู้ขับขี่จากไฟล์ JSON
        with open(json_file, 'r', encoding='utf-8') as file:
            self.data = json.load(file)  # โหลดข้อมูล JSON และเก็บในตัวแปร self.data

    def get_all_drivers(self):
        # ฟังก์ชันสำหรับคืนค่าข้อมูลผู้ขับขี่ทั้งหมด
        return self.data  # คืนค่าข้อมูลทั้งหมดที่ถูกโหลดจากไฟล์ JSON

    def get_driver_counts(self):
        # ฟังก์ชันสำหรับนับจำนวนผู้ขับขี่แยกตามประเภทและสถานะ
        driver_counts = defaultdict(lambda: defaultdict(int))  
        # ใช้ defaultdict เพื่อเก็บข้อมูลในรูปแบบซ้อน (ประเภทผู้ขับขี่ -> สถานะ -> จำนวน)

        for driver in self.data:
            driver_type = driver["Type_Driver"]  # ประเภทผู้ขับขี่ เช่น บุคคลทั่วไป, มือใหม่
            status = driver["Status"]  # สถานะของผู้ขับขี่ เช่น ปกติ, หมดอายุ, ถูกระงับ
            driver_counts[driver_type][status] += 1  # เพิ่มจำนวนผู้ขับขี่ตามประเภทและสถานะ

        return driver_counts  # คืนค่าผลลัพธ์ในรูปแบบ dictionary ซ้อน
