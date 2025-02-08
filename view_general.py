import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class GeneralView:
    def __init__(self, root, driver, controller):
        self.controller = controller
        self.root = root
        self.driver = driver

        self.frame = tk.Frame(root)
        self.frame.pack()

        # แสดงข้อมูลผู้ขับขี่
        self.label = tk.Label(self.frame, text=f"ข้อมูลผู้ขับขี่: {driver['ID_Driver']}")
        self.label.pack(pady=5)

        # แสดงสถานะของผู้ขับขี่
        self.status_label = tk.Label(self.frame, text=f"สถานะ: {driver['Status']}")
        self.status_label.pack(pady=5)

        self.age = self.controller.calculate_age(driver["Birth"])
        if self.age > 70:
            driver["Status"] = "หมดอายุ"
        elif self.age < 16:
            driver["Status"] = "ถูกระงับ"
        else:
            self.test_button = tk.Button(self.frame, text="ทดสอบสมรรถนะ", command=self.start_test)
            self.test_button.pack(pady=5)

    def start_test(self):
        self.test_button.config(text="สิ้นสุดการทดสอบ", state="disabled")
        messagebox.showinfo("ผลการทดสอบ", "การทดสอบสมรรถนะเสร็จสิ้น!")