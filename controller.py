from view_report import ReportView
from view_general import GeneralView
from view_beginner import BeginnerView
from view_public_driver import PublicDriverView
from tkinter import messagebox
import tkinter as tk
import json
import datetime

class DriverController:
    def __init__(self, model, root):
        self.model = model
        self.root = root
        self.main_menu_frame = None  # กำหนด main_menu_frame เป็น None ตอนเริ่มต้น
        self.entry_var = tk.StringVar()

    def calculate_age(self, birth_date):
        today = datetime.date.today()
        # เปลี่ยนรูปแบบวันที่จาก 'dd/mm/yyyy' เป็น datetime object
        birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y").date()  
        age = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1  # ลดอายุลง 1 ปีถ้ายังไม่ถึงวันเกิดในปีนี้
        return age

    def show_main_menu(self):
        # ทำลาย Frame เดิมถ้ามี
        if self.main_menu_frame:
            self.main_menu_frame.destroy()

        # สร้าง Frame ใหม่
        self.main_menu_frame = tk.Frame(self.root)
        self.main_menu_frame.pack()

        # เพิ่มองค์ประกอบในหน้าหลัก
        label = tk.Label(self.main_menu_frame, text="ระบบจัดการผู้ขับขี่", font=("Arial", 16))
        label.pack(pady=10)

        # ช่องกรอกข้อมูล
        entry_label = tk.Label(self.main_menu_frame, text="กรอกตัวเลข:")
        entry_label.pack(pady=5)

        entry_box = tk.Entry(self.main_menu_frame, textvariable=self.entry_var)
        entry_box.pack(pady=5)

        # ปุ่มยืนยัน
        submit_button = tk.Button(self.main_menu_frame, text="ยืนยัน", command=self.check_driver_type)
        submit_button.pack(pady=5)

        # ปุ่มรายงาน
        report_button = tk.Button(self.main_menu_frame, text="รายงาน", command=self.show_report)
        report_button.pack(pady=5)

    def submit_number(self):
        number = self.entry_var.get()  # รับค่าจากช่องกรอก
        print(f"ค่า model: {json.dumps(self.model, indent=2, ensure_ascii=False)}")
        print(f"ค่าที่กรอก: {number}")  # แสดงค่าในคอนโซล

    def check_driver_type(self):
        driver_id = self.entry_var.get().strip()

        if not driver_id:
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอก ID_Driver")
            return

        all_drivers = self.model.get_all_drivers()

        # ค้นหาคนขับตาม ID_Driver
        driver_info = next((d for d in all_drivers if d["ID_Driver"] == driver_id), None)

        if driver_info:
            driver_type = driver_info["Type_Driver"]
            # messagebox.showinfo("ผลลัพธ์", f"ID: {driver_id}\nประเภท: {driver_type}")
            
            if driver_type == "บุคคลทั่วไป":
                # self.view_general(driver_info)
                new_window = tk.Toplevel(self.root)
                GeneralView(new_window, driver_info, self)
            elif driver_type == "มือใหม่":
                # self.view_employee(driver_info)
                new_window = tk.Toplevel(self.root)
                BeginnerView(new_window, self, driver_info)
            elif driver_type == "คนขับรถสาธารณะ":
                new_window = tk.Toplevel(self.root)
                PublicDriverView(new_window, driver_info, self)
                # self.view_truck_driver(driver_info)
        else:
            messagebox.showerror("ไม่พบข้อมูล", f"ไม่มีข้อมูลของ ID: {driver_id}")

    def view_general(self, driver_info):
        messagebox.showinfo("View General", f"แสดงผลสำหรับบุคคลทั่วไป:\n{driver_info}")

    def view_employee(self, driver_info):
        messagebox.showinfo("View Employee", f"แสดงผลสำหรับพนักงานขับรถ:\n{driver_info}")

    def view_truck_driver(self, driver_info):
        messagebox.showinfo("View Truck Driver", f"แสดงผลสำหรับขับรถบรรทุก:\n{driver_info}")

    def get_driver_counts(self):
        all_drivers = self.model.get_all_drivers()  # ดึงข้อมูลผู้ขับขี่ทั้งหมด
        driver_counts = {}

        for driver in all_drivers:
            driver_type = driver["Type_Driver"]
            status = driver["Status"]

            # ถ้าไม่มีประเภทผู้ขับขี่นี้ใน driver_counts ให้เพิ่มเข้าไป
            if driver_type not in driver_counts:
                driver_counts[driver_type] = {}

            # ถ้าไม่มีสถานะนี้ในประเภทผู้ขับขี่นี้ ให้เพิ่มเข้าไป
            if status not in driver_counts[driver_type]:
                driver_counts[driver_type][status] = 0

            # เพิ่มจำนวนผู้ขับขี่ในสถานะนี้
            driver_counts[driver_type][status] += 1

        return driver_counts

    def show_report(self):
        if self.main_menu_frame:
            self.main_menu_frame.destroy()
        # เรียก View สำหรับแสดงรายงาน
        ReportView(self.root, self)
