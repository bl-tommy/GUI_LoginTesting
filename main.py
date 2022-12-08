import customtkinter as ctki


ctki.set_appearance_mode("system")
ctki.set_default_color_theme("blue")

root = ctki.CTk()
root.geometry("500x500")

def login():
    pass



frame = ctki.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctki.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

entry1 = ctki.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = ctki.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = ctki.CTkButton(master=frame, text="Login", command=login)
entry1 = ctki.CTkEntry(master=frame, placeholder_text="Username")
button.pack(pady=12, padx=10)

checkbox = ctki.CTkCheckBox(master=frame, text="Remember this browser")
checkbox.pack(pady=12, padx=10)

root.mainloop()
