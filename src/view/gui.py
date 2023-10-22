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
# View Module for MVC Design Pattern

This module serves as the `view` component in the MVC (Model-View-Controller) design pattern implemented in the project.

### Note: 
Do not execute this module as a script.

## Syntax

```
root = gui.get_root()

# Other integrations

# Start the event loop
root.mainloop()
```

- `root = gui.get_root()`: Obtain the root GUI window.
- Other integrations can be added as needed.
- `root.mainloop()`: Start the event loop for the GUI.

## Metadata
- `Author:` Aviraj Saha
- `Date:` 2023-10-08 (YYYY-MM-DD)
- `Purpose:` View module responsible for the presentation layer of the project.
"""


# imports
import tkinter as tk
from PIL import Image, ImageTk
from functools import partial
from lazy_import import lazy_module, lazy_function
from .gui_util import (
    open_url,
    launch,
    launch_visual,
    search_for_updates,
    load_urls_from_config,
    change_theme,
)
import json

# lazy Imports
logging = lazy_module("logging")
# search_for_updates = lazy_function("gui_util", "search_for_updates")
# open_url = lazy_function("gui_util", "open_url")
# launch_visual = lazy_function("gui_util", "launch_visual")
# launch_stat = lazy_function("gui_util", "launch_stat")
# load_urls_from_config = lazy_function("./gui_util.py", "load_urls_from_config")

# Globals
window = tk.Tk  # Type alias.
with open(
    "src/view/config/display_settings.json", "r", encoding="utf-8"
) as display_config_file:
    display_config = json.loads(display_config_file.read())
theme: str = display_config["theme"]

# Theme modes drop down.
themes = [
    "light",
    "dark",
]


# Hover effect
# Color update
def on_hover_color(event, button, bg_color, fg_color) -> None:
    """Changes button color on hover."""
    button.config(bg=bg_color, fg=fg_color)


# Start root window.
def get_root() -> tk.Tk:
    """
    This function prepares and returns the fully configured root window for the application.

    ### Example
    To start the event loop, use the following syntax:

    ```python
    root = get_root()
    # Other integrations
    root.mainloop()

    """
    # Load URLs from the configuration file
    urls = load_urls_from_config(r"./src/view/data/urls.json")

    # Access URLs
    readme_url: str = urls.get("readme")
    python_docs_url: str = urls.get("python_docs")
    opencv_docs_url: str = urls.get("opencv_docs")
    mediapipe_readme_url: str = urls.get("mediapipe_readme")

    # Setting up the main window.
    root: tk.Tk = tk.Tk()
    root.title("Sitfix-ai")
    root.geometry("715x535")
    root.resizable(False, False)
    root.iconbitmap("imgs/sitfixlogo.ico")

    # Setting up background window.
    if theme == "light":
        background_image: Image = Image.open("imgs/1.png")
    elif theme == "dark":
        background_image: Image = Image.open("imgs/2.png")
    else:
        raise Exception("JSON config file corrupted. Theme")
    background_photo: ImageTk.PhotoImage = ImageTk.PhotoImage(background_image)
    background_label: tk.Label = tk.Label(root, image=background_photo)
    background_label.image: ImageTk.PhotoImage = background_photo
    background_label.place(relwidth=1, relheight=1)

    # Button wedges
    update_button: tk.Button = tk.Button(
        root,
        text="Search for Updates",
        # command=search_for_updates,
        width=15,
        bg="yellow",
        fg="black",
        command=partial(search_for_updates, root=root, theme=theme),
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
        text="Calibrate",
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
        text="Launch",
        command=partial(launch, root, theme),
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
    bg_color = "white"
    fg_color = "black"
    if theme == "dark":
        bg_color = "gray14"
        fg_color = "white"

    link_readme: tk.Label = tk.Label(
        root, text="learn more.", fg=fg_color, cursor="hand2", bg=bg_color
    )
    link_readme.place(x=540, y=401)
    link_readme.bind("<Button-1>", partial(open_url, url=readme_url))

    link_python: tk.Label = tk.Label(
        root, text="Python", fg=fg_color, cursor="hand2", bg=bg_color
    )
    link_python.place(x=240, y=130)
    link_python.bind("<Button-1>", partial(open_url, url=python_docs_url))

    link_opencv: tk.Label = tk.Label(
        root, text="OpenCV", fg=fg_color, cursor="hand2", bg=bg_color
    )
    link_opencv.place(x=125, y=160)
    link_opencv.bind("<Button-1>", partial(open_url, url=opencv_docs_url))

    link_mediapipe: tk.Label = tk.Label(
        root, text="Mediapipe", fg=fg_color, cursor="hand2", bg=bg_color
    )
    link_mediapipe.place(x=50, y=160)
    link_mediapipe.bind("<Button-1>", partial(open_url, url=mediapipe_readme_url))

    # datatype of menu text
    clicked = tk.StringVar()

    # initial menu text
    clicked.set(theme)

    # Dropdowns
    drop = tk.OptionMenu(
        root,
        clicked,
        *themes,
        command=partial(change_theme, display_config=display_config),
    )

    drop.config(bg=bg_color, fg=fg_color, width=20, activebackground="yellow", padx=0)
    drop.place(x=520, y=450)
    return root


if __name__ == "__main__":
    # Configure the logging module
    logging.basicConfig(level=logging.WARNING)
    logging.warning(
        "This is the GUI module which is a part of the view portion of the app. Do not run this as a script."
    )
