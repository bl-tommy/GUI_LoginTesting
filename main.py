import customtkinter as ctki
import client, samples, socket

ctki.set_appearance_mode("system")
ctki.set_default_color_theme("blue")

root = ctki.CTk()
root.geometry("500x500")

def login():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 25545))

    message = client.recv(1024).decode()
    client.send(input(message).encode())
    message = client.recv(1024).decode()
    client.send(input(message).encode())
    print("client.recv(1024)".decode())

def register():
    root = ctki.CTk()
    root.geometry("500x500")

    frame = ctki.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctki.CTkLabel(master=frame, text="Create your account today!")
    label.pack(pady=12, padx=10)

    entry1 = ctki.CTkEntry(master=frame, placeholder_text="Create Username")
    entry1.pack(pady=12, padx=10)

    entry2 = ctki.CTkEntry(master=frame, placeholder_text="Make a Password", show="*")
    entry2.pack(pady=12, padx=10)


frame = ctki.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctki.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

entry1 = ctki.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = ctki.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = ctki.CTkButton(master=frame, text="Login", command=login)

button.pack(pady=12, padx=10)

checkbox = ctki.CTkCheckBox(master=frame, text="Remember this browser")
checkbox.pack(pady=12, padx=10)

label = ctki.CTkLabel(master=frame, text="No Account? Register Now!")
label.pack(pady=12, padx=10)

button = ctki.CTkButton(master=frame, text="Register", command=register)
button.pack(pady=12, padx=10)

root.mainloop()
