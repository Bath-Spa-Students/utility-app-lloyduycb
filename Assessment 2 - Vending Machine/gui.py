import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from time import sleep

class VendingMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vending Machine")
        self.root.geometry("600x400")

        self.menu = {
            'A1': {'item': 'Shani', 'price': 1.50, 'stock': 10},
            'A2': {'item': 'Chips Oman', 'price': 1.00, 'stock': 15},
            'A3': {'item': 'Sohar Chips', 'price': 1.00, 'stock': 15},
            'B1': {'item': 'Mai Dubai', 'price': 1.00, 'stock': 12},
            'B2': {'item': 'Zoom Candy', 'price': 0.75, 'stock': 20},
            'B3': {'item': 'Pepsi', 'price': 2.50, 'stock': 20},
            'C1': {'item': 'Mountain Dew', 'price': 2.50, 'stock': 20}
        }

        self.purchase_made = False
        self.money_entered = False
        self.current_item = None
        self.money = 0

        self.create_gui()

    def create_gui(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")  # You can experiment with other available themes

        self.label = ttk.Label(self.root, text="Vending Machine Menu", font=('Helvetica', 16, 'bold'))
        self.label.pack(pady=10)

        self.text_area = tk.Text(self.root, height=15, width=50)
        self.text_area.pack()

        self.button_buy = ttk.Button(self.root, text="Buy Item", command=self.buy_item)
        self.button_buy.pack(pady=5)

        self.button_another = ttk.Button(self.root, text="Buy Another Item", command=self.buy_another_item)
        self.button_another.pack(pady=5)

        self.button_exit = ttk.Button(self.root, text="Exit", command=self.exit_program)
        self.button_exit.pack(pady=5)

        self.display_menu()

    def display_menu(self):
        menu_text = "Vending Machine Menu:\n"
        for code, item_info in self.menu.items():
            menu_text += f"{code}: {item_info['item']} - AED {item_info['price']} ({item_info['stock']} in stock)\n"
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, menu_text)

    def buy_item(self):
        code = simpledialog.askstring("Input", "Enter item code:")
        code = code.upper()

        if code in self.menu and self.menu[code]['stock'] > 0:
            item = self.menu[code]
            self.current_item = item

            if not self.purchase_made:
                self.money = simpledialog.askinteger("Input", "Insert money:")
                while self.money <= 0:
                    messagebox.showinfo("Invalid Input", "Please enter a valid positive integer.")
                    self.money = simpledialog.askinteger("Input", "Insert money:")

                messagebox.showinfo("Money Inserted", f"You have: AED {self.money}")
                self.money_entered = True

            if self.money_entered and self.money >= item['price']:
                change = self.money - item['price']
                messagebox.showinfo("Purchase Successful", f"{item['item']} is getting dispensed.\nYour change is {change}")

                item['stock'] -= 1
                self.money = change
                self.purchase_made = True
                self.money_entered = False
            elif self.money_entered:
                messagebox.showinfo("Insufficient Funds", "Insufficient funds.")
        elif code not in self.menu:
            messagebox.showinfo("Invalid Code", "Invalid Code")
        else:
            messagebox.showinfo("Out of Stock", "Sorry, this item is out of stock.")

    def buy_another_item(self):
        self.purchase_made = False
        self.money_entered = False
        self.current_item = None
        self.money = 0
        self.display_menu()

    def exit_program(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            messagebox.showinfo("Goodbye", "Thank you for shopping with Lloyd2Go, See you next time!")
            sleep(2)
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = VendingMachineGUI(root)
    root.mainloop()
