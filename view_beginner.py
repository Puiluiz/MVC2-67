import tkinter as tk
from tkinter import messagebox

class BeginnerView:
    def __init__(self, root, controller, driver):
        self.controller = controller
        self.root = root
        self.driver = driver

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.label = tk.Label(self.frame, text=f"ข้อมูลผู้ขับขี่: {driver['ID_Driver']}")
        self.label.pack(pady=5)

        self.status_label = tk.Label(self.frame, text=f"สถานะ: {driver['Status']}")
        self.status_label.pack(pady=5)

        # คำนวณอายุ
        self.age = self.controller.calculate_age(driver["Birth"])
        if self.age > 50:
            driver["Status"] = "หมดอายุ"
        elif self.age < 16:
            driver["Status"] = "ถูกระงับ"
        else:
            # แสดงปุ่มสอบข้อเขียนและสอบปฏิบัติสำหรับ "มือใหม่" ที่อายุระหว่าง 16-50 ปี
            self.written_test_button = tk.Button(self.frame, text="สอบข้อเขียน", command=self.start_written_test)
            self.written_test_button.pack(pady=5)

            self.practice_test_button = tk.Button(self.frame, text="สอบปฏิบัติ", command=self.start_practice_test)
            self.practice_test_button.pack(pady=5)

    def start_written_test(self):
        # เมื่อกดปุ่มสอบข้อเขียน
        if self.written_test_button["text"] == "สอบข้อเขียน":
            self.written_test_button.config(text="สิ้นสุดการสอบข้อเขียน")
            messagebox.showinfo("ผลการสอบ", "การสอบข้อเขียนเสร็จสิ้น!")
        else:
            # เมื่อกดปุ่ม "สิ้นสุดการสอบข้อเขียน"
            self.written_test_button.config(state="disabled")
            self.check_all_tests_completed()

    def start_practice_test(self):
        # เมื่อกดปุ่มสอบปฏิบัติ
        if self.practice_test_button["text"] == "สอบปฏิบัติ":
            self.practice_test_button.config(text="สิ้นสุดการสอบปฏิบัติ")
            messagebox.showinfo("ผลการสอบ", "การสอบปฏิบัติเสร็จสิ้น!")
        else:
            # เมื่อกดปุ่ม "สิ้นสุดการสอบปฏิบัติ"
            self.practice_test_button.config(state="disabled")
            self.check_all_tests_completed()

    def check_all_tests_completed(self):
        # ถ้าสอบครบทั้งสองอย่างแล้ว เปลี่ยนประเภทจาก "มือใหม่" เป็น "บุคคลทั่วไป"
        if self.written_test_button["state"] == "disabled" and self.practice_test_button["state"] == "disabled":
            self.driver["Status"] = "บุคคลทั่วไป"
            self.status_label.config(text=f"สถานะ: {self.driver['Status']}")
            messagebox.showinfo("สถานะผู้ขับขี่", "ผู้ขับขี่ได้รับการอัปเกรดเป็น 'บุคคลทั่วไป'!")
