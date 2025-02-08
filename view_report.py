import tkinter as tk
from tkinter import messagebox

class ReportView:
    def __init__(self, root, controller):
        # ตัวสร้าง (Constructor) สำหรับสร้างหน้าจอรายงานจำนวนผู้ขับขี่
        self.controller = controller  # อ้างอิงไปยัง Controller
        self.root = root  # หน้าต่าง GUI หลัก

        # สร้าง Frame สำหรับแสดงเนื้อหาของหน้าจอรายงาน
        self.frame = tk.Frame(root)
        self.frame.pack()

        # แสดงหัวข้อ "รายงานจำนวนผู้ขับขี่"
        self.label = tk.Label(self.frame, text="รายงานจำนวนผู้ขับขี่", font=("Arial", 16))
        self.label.pack(pady=10)

        # สร้างพื้นที่ Text เพื่อแสดงเนื้อหารายงาน
        self.text_area = tk.Text(self.frame, width=50, height=15)
        self.text_area.pack(pady=5)

        # เรียกฟังก์ชันสร้างรายงาน
        self.generate_report()

        # ปุ่มสำหรับยืนยันการดำเนินการ
        self.confirm_button = tk.Button(self.frame, text="ยืนยัน", command=self.confirm_action)
        self.confirm_button.pack(pady=5)

        # ปุ่มสำหรับกลับไปยังหน้าหลัก
        self.back_button = tk.Button(self.frame, text="กลับ", command=self.go_back)
        self.back_button.pack(pady=10)

    def generate_report(self):
        # ฟังก์ชันสำหรับสร้างรายงานจำนวนผู้ขับขี่
        driver_counts = self.controller.get_driver_counts()  # ดึงข้อมูลจำนวนผู้ขับขี่จาก Controller
        report_text = ""  # ข้อความสำหรับแสดงผลรายงาน

        for driver_type, statuses in driver_counts.items():
            # วนลูปประเภทผู้ขับขี่และสถานะ
            report_text += f"{driver_type}:\n"
            for status, count in statuses.items():
                report_text += f"  - {status}: {count} คน\n"  # แสดงจำนวนผู้ขับขี่แยกตามสถานะ
            report_text += "\n"

        self.text_area.insert(tk.END, report_text)  # แสดงผลรายงานในพื้นที่ Text
        self.text_area.config(state="disabled")  # ปิดการแก้ไขเนื้อหาใน Text

    def confirm_action(self):
        # ฟังก์ชันสำหรับการยืนยันรายงาน
        confirm = messagebox.askyesno("ยืนยัน", "คุณต้องการยืนยันรายงานนี้หรือไม่?")  # แสดงข้อความยืนยัน
        if confirm:
            # หากผู้ใช้กด "ใช่"
            messagebox.showinfo("สำเร็จ", "การยืนยันรายงานสำเร็จ!")  # แสดงข้อความสำเร็จ
        else:
            # หากผู้ใช้กด "ไม่"
            messagebox.showinfo("ยกเลิก", "การยืนยันรายงานถูกยกเลิก!")  # แสดงข้อความยกเลิก

    def go_back(self):
        # ฟังก์ชันสำหรับกลับไปยังหน้าหลัก
        self.frame.destroy()  # ทำลาย Frame ปัจจุบัน
        self.controller.show_main_menu()  # เรียกฟังก์ชันใน Controller เพื่อแสดงหน้าหลัก
