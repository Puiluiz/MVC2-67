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
        # ตัวสร้าง (Constructor) สำหรับ Controller
        # กำหนด model และ root สำหรับ GUI และตัวแปรอื่น ๆ
        self.model = model
        self.root = root
        self.main_menu_frame = None  # กำหนดค่าเริ่มต้นให้ Frame ของเมนูหลัก
        self.entry_var = tk.StringVar()  # ตัวแปรที่เชื่อมกับ Entry สำหรับรับค่า

    def calculate_age(self, birth_date):
        # คำนวณอายุจากวันเกิด
        today = datetime.date.today()
        birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y").date()  # แปลงวันเกิดเป็น datetime object
        age = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1  # ลดอายุลง 1 ปีถ้ายังไม่ถึงวันเกิดในปีนี้
        return age

    def show_main_menu(self):
        # แสดงเมนูหลัก
        if self.main_menu_frame:
            self.main_menu_frame.destroy()  # ทำลาย Frame เดิมหากมี

        # สร้าง Frame ใหม่
        self.main_menu_frame = tk.Frame(self.root)
        self.main_menu_frame.pack()

        # แสดงหัวข้อ
        label = tk.Label(self.main_menu_frame, text="ระบบจัดการผู้ขับขี่", font=("Arial", 16))
        label.pack(pady=10)

        # ช่องกรอกข้อมูล
        entry_label = tk.Label(self.main_menu_frame, text="กรอกตัวเลข:")
        entry_label.pack(pady=5)

        entry_box = tk.Entry(self.main_menu_frame, textvariable=self.entry_var)  # เชื่อมกับ entry_var
        entry_box.pack(pady=5)

        # ปุ่มยืนยัน
        submit_button = tk.Button(self.main_menu_frame, text="ยืนยัน", command=self.check_driver_type)
        submit_button.pack(pady=5)

        # ปุ่มรายงาน
        report_button = tk.Button(self.main_menu_frame, text="รายงาน", command=self.show_report)
        report_button.pack(pady=5)

    def submit_number(self):
        # สำหรับแสดงข้อมูลในคอนโซล (ทดสอบ)
        number = self.entry_var.get()  # รับค่าจากช่องกรอก
        print(f"ค่า model: {json.dumps(self.model, indent=2, ensure_ascii=False)}")
        print(f"ค่าที่กรอก: {number}")  # แสดงค่าในคอนโซล

    def check_driver_type(self):
        # ตรวจสอบประเภทผู้ขับขี่ตาม ID_Driver
        driver_id = self.entry_var.get().strip()

        if not driver_id:
            # แสดงข้อความข้อผิดพลาดหากไม่ได้กรอก ID
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอก ID_Driver")
            return

        # ดึงข้อมูลผู้ขับขี่ทั้งหมด
        all_drivers = self.model.get_all_drivers()

        # ค้นหาผู้ขับขี่จาก ID_Driver
        driver_info = next((d for d in all_drivers if d["ID_Driver"] == driver_id), None)

        if driver_info:
            # ตรวจสอบประเภทผู้ขับขี่และแสดง View ที่เหมาะสม
            driver_type = driver_info["Type_Driver"]
            if driver_type == "บุคคลทั่วไป":
                new_window = tk.Toplevel(self.root)  # สร้างหน้าต่างใหม่
                GeneralView(new_window, driver_info, self)
            elif driver_type == "มือใหม่":
                new_window = tk.Toplevel(self.root)
                BeginnerView(new_window, self, driver_info)
            elif driver_type == "คนขับรถสาธารณะ":
                new_window = tk.Toplevel(self.root)
                PublicDriverView(new_window, driver_info, self)
        else:
            # แสดงข้อผิดพลาดหากไม่พบข้อมูลผู้ขับขี่
            messagebox.showerror("ไม่พบข้อมูล", f"ไม่มีข้อมูลของ ID: {driver_id}")

    def view_general(self, driver_info):
        # แสดงข้อมูลสำหรับ "บุคคลทั่วไป"
        messagebox.showinfo("View General", f"แสดงผลสำหรับบุคคลทั่วไป:\n{driver_info}")

    def view_employee(self, driver_info):
        # แสดงข้อมูลสำหรับ "พนักงานขับรถ"
        messagebox.showinfo("View Employee", f"แสดงผลสำหรับพนักงานขับรถ:\n{driver_info}")

    def view_truck_driver(self, driver_info):
        # แสดงข้อมูลสำหรับ "คนขับรถบรรทุก"
        messagebox.showinfo("View Truck Driver", f"แสดงผลสำหรับขับรถบรรทุก:\n{driver_info}")

    def get_driver_counts(self):
        # นับจำนวนผู้ขับขี่ในแต่ละประเภทและสถานะ
        all_drivers = self.model.get_all_drivers()  # ดึงข้อมูลผู้ขับขี่ทั้งหมด
        driver_counts = {}

        for driver in all_drivers:
            driver_type = driver["Type_Driver"]
            status = driver["Status"]

            # จัดประเภทผู้ขับขี่และสถานะ
            if driver_type not in driver_counts:
                driver_counts[driver_type] = {}
            if status not in driver_counts[driver_type]:
                driver_counts[driver_type][status] = 0
            driver_counts[driver_type][status] += 1

        return driver_counts

    def show_report(self):
        # แสดงรายงานผู้ขับขี่
        if self.main_menu_frame:
            self.main_menu_frame.destroy()  # ทำลาย Frame ปัจจุบัน
        ReportView(self.root, self)  # สร้างหน้าจอรายงานใหม่
