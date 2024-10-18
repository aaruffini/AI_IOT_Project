import tkinter as tk
from tkinter import messagebox
import LastFMLogin
def setup():
    def button_clicked():
        LastFMLogin.login()

    root = tk.Tk()
    root.title("Music Lights")
    root.config(bg="#3e0b00")
    root.geometry("1000x1000")
    # Main Label
    mainLabel = tk.Label(text="Welcome to my app! "
                              "\n\n Click the button below to login to your lastFM Account.",

                         font=("Courier New", 18, "bold"),
                         bg = "#320900"
                         )
    mainLabel.pack(pady=100)
    # Login button
    logInButton = tk.Button(text="Click Here to log in",
                            command=button_clicked,
                            bg = "#3e0b00",
                            fg= "#320900",


                            )


    logInButton.pack(pady= 10)

    root.mainloop()

