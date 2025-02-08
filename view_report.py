import tkinter as tk
from tkinter import messagebox

class ReportView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root

        self.frame = tk.Frame(root)
        self.frame.pack()

        # หัวข้อรายงาน
        self.label = tk.Label(self.frame, text="รายงานจำนวนผู้ขับขี่", font=("Arial", 16))
        self.label.pack(pady=10)

        # พื้นที่แสดงรายงาน
        self.text_area = tk.Text(self.frame, width=50, height=15)
        self.text_area.pack(pady=5)

        # สร้างรายงาน
        self.generate_report()

        # ปุ่มยืนยัน
        self.confirm_button = tk.Button(self.frame, text="ยืนยัน", command=self.confirm_action)
        self.confirm_button.pack(pady=5)

        # ปุ่มกลับไปหน้าหลัก
        self.back_button = tk.Button(self.frame, text="กลับ", command=self.go_back)
        self.back_button.pack(pady=10)

    def generate_report(self):
        driver_counts = self.controller.get_driver_counts()
        report_text = ""

        for driver_type, statuses in driver_counts.items():
            report_text += f"{driver_type}:\n"
            for status, count in statuses.items():
                report_text += f"  - {status}: {count} คน\n"
            report_text += "\n"

        self.text_area.insert(tk.END, report_text)
        self.text_area.config(state="disabled")

    def confirm_action(self):
        # ฟังก์ชันสำหรับการยืนยัน
        confirm = messagebox.askyesno("ยืนยัน", "คุณต้องการยืนยันรายงานนี้หรือไม่?")
        if confirm:
            messagebox.showinfo("สำเร็จ", "การยืนยันรายงานสำเร็จ!")
        else:
            messagebox.showinfo("ยกเลิก", "การยืนยันรายงานถูกยกเลิก!")

    def go_back(self):
        # กลับไปหน้าหลัก
        self.frame.destroy()
        self.controller.show_main_menu()
