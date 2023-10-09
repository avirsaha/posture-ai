# MIT License
# Copyright (c) 2023 The_BDMI_Students_Exhibition_Team_2023
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""This is a gui script of running the software.
"""
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import main
import logging


__author__: str = "Aviraj Saha"
__date__: str = "2023-10-8"
__purpose__: str = "This is a gui script of running the software."
__metadata__: tuple[str, ...] = None


# Configure the logging module
logging.basicConfig(level=logging.INFO)  # Set the logging level to INFO


# Utilitity methods
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


# App beginning
def main() -> None:
    """
    This is where the execution
    """

    # Hover effects
    # Set 1
    def on_hover_version(event) -> None:
        """Changes button color on hover."""
        update_button.config(bg="black", fg="white")

    def on_leave_version(event) -> None:
        """Changes button color back to black when not hovered."""
        update_button.config(bg="yellow", fg="black")

    # Set 2
    def on_hover_launch_visual(event) -> None:
        """Changes button color on hover."""
        launch_button_visual.config(bg="yellow", fg="black")

    def on_leave_launch_visual(event) -> None:
        """Changes button color back to black when not hovered."""
        launch_button_visual.config(bg="black", fg="white")

    # Set 3
    def on_hover_launch_stat(event) -> None:
        """Changes button color on hover."""
        launch_button_stat.config(bg="yellow", fg="black")

    def on_leave_launch_stat(event) -> None:
        """Changes button color back to black when not hovered."""
        launch_button_stat.config(bg="black", fg="white")

    # Setting up the main window.
    root: tk.Tk = tk.Tk()
    root.title("Sitfix-ai")
    root.geometry("715x535")
    root.resizable(False, False)
    root.iconbitmap("imgs/sitfixlogo.ico")

    # Setting up background window.
    background_image: Image = Image.open("imgs/Sitfix-ai-home3.png")
    background_photo: ImageTk.PhotoImage = ImageTk.PhotoImage(background_image)
    background_label: tk.Label = tk.Label(root, image=background_photo)
    background_label.image: ImageTk.PhotoImage = background_photo
    background_label.place(relwidth=1, relheight=1)

    # Button wedges
    update_button: tk.Button = tk.Button(
        root,
        text="Search for Updates",
        command=search_for_updates,
        width=15,
        bg="yellow",
        fg="black",
    )
    update_button.place(x=460, y=130)
    update_button.bind("<Enter>", on_hover_version)
    update_button.bind("<Leave>", on_leave_version)

    launch_button_visual: tk.Button = tk.Button(
        root,
        text="Launch Visual",
        command=launch_app,
        width=12,
        bg="black",
        fg="white",
    )
    launch_button_visual.place(x=460, y=270)
    launch_button_visual.bind("<Enter>", on_hover_launch_visual)
    launch_button_visual.bind("<Leave>", on_leave_launch_visual)

    launch_button_stat: tk.Button = tk.Button(
        root,
        text="Launch Stat",
        command=launch_app,
        width=12,
        bg="Black",
        fg="White",
    )
    launch_button_stat.place(x=565, y=270)
    launch_button_stat.bind("<Enter>", on_hover_launch_stat)
    launch_button_stat.bind("<Leave>", on_leave_launch_stat)

    # Links
    link_readme: tk.Label = tk.Label(
        root, text="learn more.", fg="blue", cursor="hand2"
    )
    link_readme.place(x=540, y=401)
    link_readme.bind(
        "<Button-1>", lambda e: callback("https://github.com/avirsaha/sitfix-ai#readme")
    )

    link_python: tk.Label = tk.Label(root, text="Python", fg="blue", cursor="hand2")
    link_python.place(x=240, y=130)
    link_python.bind("<Button-1>", lambda e: callback("https://docs.python.org/3.11/"))

    link_mediapipe: tk.Label = tk.Label(
        root, text="Mediapipe", fg="blue", cursor="hand2"
    )
    link_mediapipe.place(x=50, y=160)
    link_mediapipe.bind(
        "<Button-1>", lambda e: callback("https://github.com/google/mediapipe#readme")
    )

    link_opencv: tk.Label = tk.Label(root, text="OpenCV", fg="blue", cursor="hand2")
    link_opencv.place(x=125, y=160)
    link_opencv.bind(
        "<Button-1>", lambda e: callback("https://docs.opencv.org/4.x/index.html")
    )

    # Event loop
    root.mainloop()


if __name__ == "__main__":
    main()
