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
"""
This module acts as the view module for the MCV Design pattern followed by the project.
Do not run this as a script.

:syntax::
root = gui.get_root()

# Other integrations

# Start the event loop
root.mainloop()

:Metadata::
:author: Aviraj Saha
:date: 2023-10-08 | YYYY-MM-DD
:purpose: View module of the project.
"""


# imports
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from functools import partial
from lazy_import import lazy_module, lazy_function
from gui_util import open_url, launch_stat, launch_visual, search_for_updates

# lazy Imports
logging = lazy_module("logging")
# search_for_updates = lazy_function("gui_util", "search_for_updates")
# open_url = lazy_function("gui_util", "open_url")
# launch_visual = lazy_function("gui_util", "launch_visual")
# launch_stat = lazy_function("gui_util", "launch_stat")
load_urls_from_config = lazy_function("gui_util", "load_urls_from_config")


# Hover effect
# Color update
def on_hover_color(event, button, bg_color, fg_color) -> None:
    """Changes button color on hover."""
    button.config(bg=bg_color, fg=fg_color)


# Start root window.
def get_root() -> tk.Tk:
    """
    This function returns fully prepared root window.

    :syntax::
    start the event loop by:
    root = gui.start_app()
    root.mainloop()

    Returns:
        tk.Tk: Fully build root window of the app.
    """

    # Load URLs from the configuration file
    urls = load_urls_from_config("urls.json")

    # Access URLs
    readme_url = urls.get("readme")
    python_docs_url = urls.get("python_docs")
    opencv_docs_url = urls.get("opencv_docs")
    mediapipe_readme_url = urls.get("mediapipe_readme")

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
    update_button.bind(
        "<Enter>",
        partial(
            on_hover_color, button=update_button, bg_color="black", fg_color="white"
        ),
    )
    update_button.bind(
        "<Leave>",
        partial(
            on_hover_color, button=update_button, bg_color="yellow", fg_color="black"
        ),
    )

    launch_button_visual: tk.Button = tk.Button(
        root,
        text="Launch Visual",
        command=launch_visual,
        width=12,
        bg="black",
        fg="white",
    )
    launch_button_visual.place(x=460, y=270)
    launch_button_visual.bind(
        "<Enter>",
        partial(
            on_hover_color,
            button=launch_button_visual,
            bg_color="yellow",
            fg_color="black",
        ),
    )
    launch_button_visual.bind(
        "<Leave>",
        partial(
            on_hover_color,
            button=launch_button_visual,
            bg_color="black",
            fg_color="white",
        ),
    )

    launch_button_stat: tk.Button = tk.Button(
        root,
        text="Launch Stat",
        command=launch_stat,
        width=12,
        bg="Black",
        fg="yellow",
    )
    launch_button_stat.place(x=565, y=270)
    launch_button_stat.bind(
        "<Enter>",
        partial(
            on_hover_color,
            button=launch_button_stat,
            bg_color="yellow",
            fg_color="black",
        ),
    )
    launch_button_stat.bind(
        "<Leave>",
        partial(
            on_hover_color,
            button=launch_button_stat,
            bg_color="black",
            fg_color="yellow",
        ),
    )

    # Links
    link_readme: tk.Label = tk.Label(
        root, text="learn more.", fg="blue", cursor="hand2"
    )
    link_readme.place(x=540, y=401)
    link_readme.bind("<Button-1>", partial(open_url, url=readme_url))

    link_python: tk.Label = tk.Label(root, text="Python", fg="black", cursor="hand2")
    link_python.place(x=240, y=130)
    link_python.bind("<Button-1>", partial(open_url, url=python_docs_url))

    link_opencv: tk.Label = tk.Label(root, text="OpenCV", fg="black", cursor="hand2")
    link_opencv.place(x=125, y=160)
    link_opencv.bind("<Button-1>", partial(open_url, url=opencv_docs_url))

    link_mediapipe: tk.Label = tk.Label(
        root, text="Mediapipe", fg="black", cursor="hand2"
    )
    link_mediapipe.place(x=50, y=160)
    link_mediapipe.bind("<Button-1>", partial(open_url, url=mediapipe_readme_url))

    return root


if __name__ == "__main__":
    # Configure the logging module
    logging.basicConfig(level=logging.WARNING)
    logging.warning(
        "This is the GUI module which is a part of the view portion of the app. Do not run this as a script."
    )
