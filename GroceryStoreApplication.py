
import tkinter as tk
from tkinter import messagebox
import csv

# Load products from a CSV file
def load_products(file_path):
    products = {}
    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products[row["Name"]] = int(row["Price"])
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {file_path} not found!")
    return products
# Load products from CSV
products_file = "products.csv"
items = load_products(products_file)
cart = {}

def add_to_cart(item):
    if item in cart:
        cart[item] += 1
    else:
        cart[item] = 1
    update_cart_display()

def remove_from_cart(item):
    if item in cart:
        if cart[item] > 1:
            cart[item] -= 1
        else:
            del cart[item]
    update_cart_display()

def update_cart_display():
    cart_list.delete(0, tk.END)  # Clear the listbox
    total = 0
    for item, quantity in cart.items():
        price = items[item] * quantity
        total += price
        cart_list.insert(tk.END, f"{item} x{quantity} = ₹{price}")
    total_label.config(text=f"Total: ₹{total}")

def checkout()
    if not cart:
        messagebox.showinfo("Checkout", "Your cart is empty!")
    else:
        total = sum(items[item] * quantity for item, quantity in cart.items())
        messagebox.showinfo("Checkout", f"Total Bill: ₹{total}\nThank you for shopping!")
        cart.clear()
        update_cart_display()

# Create the main application window
app = tk.Tk()
app.title("Grocery Store App")
app.geometry("400x600")

# Product list
product_frame = tk.Frame(app)
product_frame.pack(pady=10)

tk.Label(product_frame, text="Available Items", font=("Arial", 16)).pack()
for item, price in items.items():
    tk.Button(
        product_frame,
        text=f"{item} - ₹{price}",
        command=lambda i=item: add_to_cart(i)
    ).pack(fill=tk.X, pady=2)

# Cart 
cart_frame = tk.Frame(app)
cart_frame.pack(pady=10)

tk.Label(cart_frame, text="Your Cart", font=("Arial", 16)).pack()
cart_list = tk.Listbox(cart_frame, width=40, height=10)
cart_list.pack()

# Total and Checkout 
total_label = tk.Label(cart_frame, text="Total: ₹0", font=("Arial", 14))
total_label.pack(pady=5)

tk.Button(cart_frame, text="Checkout", command=checkout).pack(pady=5)
tk.Button(cart_frame, text="Remove Selected", command=lambda: remove_from_cart(cart_list.get(tk.ACTIVE).split(" x")[0] if cart_list.curselection() else None)).pack()

# Run the application
app.mainloop()
