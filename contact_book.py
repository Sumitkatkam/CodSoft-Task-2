import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = {}

        # Frames
        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack(pady=10)

        self.frame_display = tk.Frame(root)
        self.frame_display.pack(pady=10)

        # Buttons
        self.btn_add = tk.Button(self.frame_buttons, text="Add Contact", command=self.add_contact)
        self.btn_add.pack(side=tk.LEFT, padx=5)

        self.btn_view = tk.Button(self.frame_buttons, text="View Contacts", command=self.view_contacts)
        self.btn_view.pack(side=tk.LEFT, padx=5)

        self.btn_search = tk.Button(self.frame_buttons, text="Search Contact", command=self.search_contact)
        self.btn_search.pack(side=tk.LEFT, padx=5)

        self.btn_update = tk.Button(self.frame_buttons, text="Update Contact", command=self.update_contact)
        self.btn_update.pack(side=tk.LEFT, padx=5)

        self.btn_delete = tk.Button(self.frame_buttons, text="Delete Contact", command=self.delete_contact)
        self.btn_delete.pack(side=tk.LEFT, padx=5)

        # Display Area
        self.display_text = tk.Text(self.frame_display, height=20, width=50)
        self.display_text.pack()

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        if name:
            phone = simpledialog.askstring("Input", "Enter Phone Number:")
            email = simpledialog.askstring("Input", "Enter Email:")
            address = simpledialog.askstring("Input", "Enter Address:")
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            messagebox.showinfo("Info", "Contact added successfully!")

    def view_contacts(self):
        self.display_text.delete('1.0', tk.END)
        if not self.contacts:
            self.display_text.insert(tk.END, "No contacts available.\n")
        else:
            for name, details in self.contacts.items():
                self.display_text.insert(tk.END, f"Name: {name}\n")
                self.display_text.insert(tk.END, f"Phone: {details['phone']}\n")
                self.display_text.insert(tk.END, f"Email: {details['email']}\n")
                self.display_text.insert(tk.END, f"Address: {details['address']}\n\n")

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter Name or Phone Number to Search:")
        self.display_text.delete('1.0', tk.END)
        found = False
        for name, details in self.contacts.items():
            if query in name or query in details['phone']:
                self.display_text.insert(tk.END, f"Name: {name}\n")
                self.display_text.insert(tk.END, f"Phone: {details['phone']}\n")
                self.display_text.insert(tk.END, f"Email: {details['email']}\n")
                self.display_text.insert(tk.END, f"Address: {details['address']}\n\n")
                found = True
        if not found:
            self.display_text.insert(tk.END, "No matching contact found.\n")

    def update_contact(self):
        name = simpledialog.askstring("Update", "Enter the Name of the Contact to Update:")
        if name and name in self.contacts:
            phone = simpledialog.askstring("Input", "Enter New Phone Number:")
            email = simpledialog.askstring("Input", "Enter New Email:")
            address = simpledialog.askstring("Input", "Enter New Address:")
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            messagebox.showinfo("Info", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete", "Enter the Name of the Contact to Delete:")
        if name and name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Info", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
