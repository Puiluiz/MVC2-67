import tkinter as tk
from model import DriverModel
from controller import DriverController

if __name__ == "__main__":
    # โหลด Model
    model = DriverModel("drivers.json")

    # สร้าง GUI
    root = tk.Tk()
    controller = DriverController(model, root)  # สร้าง Controller

    # เรียกหน้าหลัก
    controller.show_main_menu()

    # เริ่มแอปพลิเคชัน
    root.mainloop()
