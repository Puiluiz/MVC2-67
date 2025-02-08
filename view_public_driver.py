import tkinter as tk
from tkinter import messagebox
import random

class PublicDriverView:
    def __init__(self, root, driver, controller):
        self.controller = controller
        self.root = root
        self.driver = driver

        self.frame = tk.Frame(root)
        self.frame.pack()

         # แสดงข้อมูลผู้ขับขี่
        self.label = tk.Label(self.frame, text=f"ข้อมูลผู้ขับขี่: {driver['ID_Driver']}")
        self.label.pack(pady=5)

        self.status_label = tk.Label(self.frame, text=f"สถานะ: {driver['Status']}")
        self.status_label.pack(pady=5)

        self.age = self.controller.calculate_age(driver["Birth"])
        if self.age > 60:
            driver["Status"] = "หมดอายุ"
        elif self.age < 20:
            driver["Status"] = "ถูกระงับ"
        else:
            complaints = random.randint(0, 10)
            complaint_label = tk.Label(self.frame, text=f"จำนวนการร้องเรียน: {complaints}")
            complaint_label.pack(pady=5)

            if complaints > 5:
                driver["Status"] = "ถูกระงับชั่วคราว"
                self.training_button = tk.Button(self.frame, text="อบรม", command=self.start_training)
                self.training_button.pack(pady=5)
            else:
                self.test_button = tk.Button(self.frame, text="ทดสอบสมรรถนะ", command=self.start_test)
                self.test_button.pack(pady=5)

        # อัปเดต label สถานะ
        self.status_label.config(text=f"สถานะ: {driver['Status']}")


    def start_training(self):
        self.training_button.config(text="สิ้นสุดการอบรม", state="disabled")
        messagebox.showinfo("ผลการอบรม", "การอบรมเสร็จสิ้น!")
        self.driver["Status"] = "ปกติ"

    def start_test(self):
        self.test_button.config(text="สิ้นสุดการทดสอบ", state="disabled")
        messagebox.showinfo("ผลการทดสอบ", "การทดสอบสมรรถนะเสร็จสิ้น!")