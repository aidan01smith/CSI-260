import tkinter as tk
from tkinter import messagebox

class BasicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("the application.")
        self.root.geometry("500x400")

        # Label
        self.label = tk.Label(root, text="Welcome to Tkinter OOP!", font=("Arial", 14))
        self.label.pack(pady=20)

        # Buttons
        self.change_text_button = tk.Button(root, text="Change Text", command=self.change_text)
        self.change_text_button.pack(pady=5)

        self.show_message_button = tk.Button(root, text="Show Message", command=self.show_message)
        self.show_message_button.pack(pady=5)

        self.quit_button = tk.Button(root, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=5)

        # Adding the CounterApp class
        self.counter_app = CounterApp(root)

    def change_text(self):
        self.label.config(text="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    def show_message(self):
        messagebox.showinfo("Message", "I AM IN PAIN SO MUCH PAIN!")

class CounterApp:
    def __init__(self, root):
        self.counter = 0

        # Counter Label
        self.counter_label = tk.Label(root, text=f"Counter: {self.counter}", font=("Arial", 14))
        self.counter_label.pack(pady=10)

        # Buttons to increment and decrement
        self.increment_button = tk.Button(root, text="me when I increase the number", command=self.increment)
        self.increment_button.pack(pady=5)

        self.decrement_button = tk.Button(root, text="me when I decrease the number", command=self.decrement)
        self.decrement_button.pack(pady=5)

    def increment(self):
        self.counter += 1
        self.update_label()

    def decrement(self):
        self.counter -= 1
        self.update_label()

    def update_label(self):
        self.counter_label.config(text=f"Counter: {self.counter}")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = BasicApp(root)
    root.mainloop()
