import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import main

def search_for_updates() -> None:
    """Handles the search for updates button click event."""
    messagebox.showinfo("Search for Updates", "Checking for updates...")

def callback(url) -> None:
    """Opens a URL in the default web browser."""
    webbrowser.open_new_tab(url)

def launch_app() -> None:
    """Handles the launch button click event."""
    result = messagebox.askyesno("Launch App", "Do you want to start monitoring...")
    if result:
        main.main()


def main() -> None:
    """
    This is where the execution
    """
    def on_hover(event) -> None:
        """Changes button color on hover."""
        update_button.config(bg="yellow", fg="black")

    def on_leave(event) -> None:
        """Changes button color back to black when not hovered."""
        update_button.config(bg="black", fg="white")



    root = tk.Tk()
    root.title("Sitfix-ai")
    root.geometry("715x535")
    root.resizable(False, False)
    root.iconbitmap("imgs/sitfixlogo.ico")

    background_image = Image.open("imgs/Sitfix-ai-home3.png")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(relwidth=1, relheight=1)

    update_button = tk.Button(
        root,
        text="Search for Updates",
        command=search_for_updates,
        width=15,
        bg="black",
        fg="white",
    )
    update_button.place(x=460, y=130)

    link_readme = tk.Label(root, text="learn more.", fg="blue", cursor="hand2")
    link_readme.place(x=540, y=401)
    link_readme.bind("<Button-1>", lambda e: callback("https://github.com/avirsaha/sitfix-ai#readme"))

    launch_button1 = tk.Button(
        root, text="Launch Visual", command=launch_app, width=12, bg="Yellow", fg="black"
    )
    launch_button1.place(x=460, y=270)

    launch_button2 = tk.Button(
        root, text="Launch Stat", command=launch_app, width=12, bg="Black", fg="White"
    )
    launch_button2.place(x=565, y=270)

    update_button.bind("<Enter>", on_hover)
    update_button.bind("<Leave>", on_leave)

    root.mainloop()

if __name__ == "__main__":
    main()