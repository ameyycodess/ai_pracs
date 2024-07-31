import tkinter as tk
from tkinter import simpledialog, messagebox

class WaterJugGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Jug")
        self.root.configure(bg="black")

        
        self.jugA_capacity = simpledialog.askinteger("Water Jug Problem", "Enter the capacity of Jug A (2 to 10 liters):", minvalue=2, maxvalue=10)
        self.jugB_capacity = simpledialog.askinteger("Water Jug Problem", "Enter the capacity of Jug B (2 to 10 liters):", minvalue=2, maxvalue=10)
        self.target = simpledialog.askinteger("Water Jug Problem", "Enter the target amount (1 to 10 liters):", minvalue=1, maxvalue=10)

        if self.jugA_capacity is None or self.jugB_capacity is None or self.target is None:
            self.root.destroy()
            return

        
        self.jugA = 0
        self.jugB = 0

        self.create_widgets()
        self.update_display()

    def create_widgets(self):
        self.jugA_label = tk.Label(self.root, text=f"Jug A: {self.jugA}/{self.jugA_capacity} L", font=("Arial", 16), bg="lightblue")
        self.jugA_label.pack(pady=10)

        self.jugB_label = tk.Label(self.root, text=f"Jug B: {self.jugB}/{self.jugB_capacity} L", font=("Arial", 16), bg="lightblue")
        self.jugB_label.pack(pady=10)

        self.fillA_button = tk.Button(self.root, text="Fill Jug A", command=self.fill_jugA, font=("Arial", 14), bg="green", fg="white")
        self.fillA_button.pack(pady=5)

        self.fillB_button = tk.Button(self.root, text="Fill Jug B", command=self.fill_jugB, font=("Arial", 14), bg="green", fg="white")
        self.fillB_button.pack(pady=5)

        self.emptyA_button = tk.Button(self.root, text="Empty Jug A", command=self.empty_jugA, font=("Arial", 14), bg="red", fg="white")
        self.emptyA_button.pack(pady=5)

        self.emptyB_button = tk.Button(self.root, text="Empty Jug B", command=self.empty_jugB, font=("Arial", 14), bg="red", fg="white")
        self.emptyB_button.pack(pady=5)

        self.pourAB_button = tk.Button(self.root, text="Pour Jug A into Jug B", command=self.pour_A_to_B, font=("Arial", 14), bg="blue", fg="white")
        self.pourAB_button.pack(pady=5)

        self.pourBA_button = tk.Button(self.root, text="Pour Jug B into Jug A", command=self.pour_B_to_A, font=("Arial", 14), bg="blue", fg="white")
        self.pourBA_button.pack(pady=5)


        self.check_button = tk.Button(self.root, text="Check Solution", command=self.check_solution, font=("Arial", 14), bg="orange", fg="white")
        self.check_button.pack(pady=10)

    def update_display(self):
        self.jugA_label.config(text=f"Jug A: {self.jugA}/{self.jugA_capacity} L")
        self.jugB_label.config(text=f"Jug B: {self.jugB}/{self.jugB_capacity} L")

    def fill_jugA(self):
        self.jugA = self.jugA_capacity
        self.update_display()

    def fill_jugB(self):
        self.jugB = self.jugB_capacity
        self.update_display()

    def empty_jugA(self):
        self.jugA = 0
        self.update_display()

    def empty_jugB(self):
        self.jugB = 0
        self.update_display()

    def pour_A_to_B(self):
        pour_amount = min(self.jugA, self.jugB_capacity - self.jugB)
        self.jugA -= pour_amount
        self.jugB += pour_amount
        self.update_display()

    def pour_B_to_A(self):
        pour_amount = min(self.jugB, self.jugA_capacity - self.jugA)
        self.jugB -= pour_amount
        self.jugA += pour_amount
        self.update_display()

    def check_solution(self):
        if self.jugA == self.target or self.jugB == self.target:
            messagebox.showinfo("Success!", f"You successfully measured {self.target} liters!")
        else:
            messagebox.showerror("Try Again", f"You have not measured {self.target} liters yet. Keep trying!")

if __name__ == "__main__":
    root = tk.Tk()
    game = WaterJugGame(root)
    root.mainloop()
