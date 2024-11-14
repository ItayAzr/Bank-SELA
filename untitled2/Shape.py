import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Main Application Class
class MoneyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Money Giving and Receiving App")
        self.root.geometry("600x400")
        self.root.config(bg="#f8f8f8")  # Light background color

        self.balance = 0  # Initial balance set to zero

        # Set up modern fonts and colors
        self.heading_font = ("Helvetica Neue", 20, "bold")
        self.label_font = ("Arial", 12)
        self.button_font = ("Arial", 12, "bold")

        # Colors for buttons and background
        self.primary_color = "#3b9d7d"  # Greenish
        self.secondary_color = "#F3A847"  # Orange
        self.bg_color = "#f8f8f8"
        self.button_hover_color = "#2a7a5d"  # Darker green
        self.button_active_color = "#f27b21"  # Active state color for button
        self.entry_bg_color = "#f1f1f1"  # Light gray for entry box

        # Title Label
        self.title_label = tk.Label(self.root, text="Money App", font=self.heading_font, bg=self.bg_color, fg="#333")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Balance display
        self.balance_label = tk.Label(self.root, text=f"Balance: ${self.balance:.2f}", font=self.label_font,
                                      bg=self.bg_color, fg="#333")
        self.balance_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Amount Entry label
        self.amount_label = tk.Label(self.root, text="Enter Amount:", font=self.label_font, bg=self.bg_color, fg="#333")
        self.amount_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        # Amount Entry field with rounded corners and subtle shadow
        self.amount_entry = tk.Entry(self.root, font=("Arial", 12), width=20, borderwidth=2, relief="flat",
                                     bg=self.entry_bg_color, highlightbackground="#ddd", highlightthickness=1)
        self.amount_entry.grid(row=2, column=1, pady=10, padx=20)

        # Give Money Button
        self.give_button = tk.Button(self.root, text="Give Money", font=self.button_font, fg="white",
                                     bg=self.primary_color,
                                     command=self.give_money, relief="flat", height=2, width=15)
        self.give_button.grid(row=3, column=0, pady=20, padx=10, sticky="nsew")
        self.give_button.bind("<Enter>", self.on_enter)
        self.give_button.bind("<Leave>", self.on_leave)
        self.give_button.bind("<Button-1>", self.on_click)

        # Receive Money Button
        self.receive_button = tk.Button(self.root, text="Receive Money", font=self.button_font, fg="white",
                                        bg=self.secondary_color,
                                        command=self.receive_money, relief="flat", height=2, width=15)
        self.receive_button.grid(row=3, column=1, pady=20, padx=10, sticky="nsew")
        self.receive_button.bind("<Enter>", self.on_enter)
        self.receive_button.bind("<Leave>", self.on_leave)
        self.receive_button.bind("<Button-1>", self.on_click)

        # Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", font=self.button_font, fg="white", bg="#607D8B",
                                     command=self.root.quit, relief="flat", height=2, width=15)
        self.exit_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Configure grid rows and columns to resize properly
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def update_balance(self):
        # Update the balance label
        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")

    def give_money(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Invalid Amount", "Amount to give must be positive!")
                return
            if amount > self.balance:
                messagebox.showerror("Insufficient Funds", "You do not have enough balance!")
                return
            self.balance -= amount
            self.update_balance()
            messagebox.showinfo("Transaction Successful", f"You have successfully given ${amount}.")
            self.amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number!")

    def receive_money(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Invalid Amount", "Amount to receive must be positive!")
                return
            self.balance += amount
            self.update_balance()
            messagebox.showinfo("Transaction Successful", f"You have successfully received ${amount}.")
            self.amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number!")

    def on_enter(self, event):
        # Change button color on hover
        event.widget.config(bg=self.button_hover_color)

    def on_leave(self, event):
        # Restore button color when not hovering
        if event.widget == self.give_button:
            event.widget.config(bg=self.primary_color)
        elif event.widget == self.receive_button:
            event.widget.config(bg=self.secondary_color)

    def on_click(self, event):
        # Change button color on click (active state)
        event.widget.config(bg=self.button_active_color)


def play():
    # Set up the main Tkinter window
    root = tk.Tk()

    # Create an instance of the MoneyApp
    app = MoneyApp(root)

    # Run the Tkinter event loop
    root.mainloop()
