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
This module contains utilities for the `view` module following the MVC (Model-View-Controller) design pattern used in the project.

### Note:
 Do not run this module as a script.

## Metadata
- `Author:` Aviraj Saha
- `Date:` 2023-10-08 (YYYY-MM-DD)
- `Purpose:` Utility functions for the Graphical User Interface (GUI) component of the project.
"""

# Imports
import tkinter as tk
from lazy_import import lazy_function, lazy_module
from tkinter import messagebox
from webbrowser import open_new_tab
from PIL import Image, ImageTk

# Lazy Imports
# open_new_tab = lazy_function("webbrowser", "open_new_tab")
logging = lazy_module("logging")
json = lazy_module("json")


# Utility functions for GUI.


def change_theme(value, display_config):
    display_config["theme"] = value
    json_object = json.dumps(display_config, indent=4)
    with open(
        "src/view/config/display_settings.json", "w", encoding="utf-8"
    ) as display_config_file:
        display_config_file.write(json_object)
    messagebox.showinfo(
        "Sitfix-ai Alert!", message="Restart the program to see changes made."
    )


def search_for_updates(root, theme) -> None:
    """
    Handles the event when the "Search for Updates" button is clicked. It displays an informational message box indicating that the application is checking for updates.

    ### Parameters
    This function takes no parameters.

    ### Returns
    This function does not return any value (`None`).

    ### Side Effects
    Displays an informational message box with the message "Checking for updates..."

    ### Example
    ```python
    search_for_updates()"""
    updates_window = tk.Toplevel(root)
    updates_window.title("Sitfix-ai Updates")
    updates_window.geometry("715x535")
    updates_window.resizable(False, False)
    updates_window.iconbitmap("imgs/sitfixlogo.ico")

    # Setting up background window.
    if theme == "light":
        background_image: Image = Image.open("imgs/3.png")
    elif theme == "dark":
        background_image: Image = Image.open("imgs/4.png")

    background_photo: ImageTk.PhotoImage = ImageTk.PhotoImage(background_image)
    background_label: tk.Label = tk.Label(updates_window, image=background_photo)
    background_label.image: ImageTk.PhotoImage = background_photo
    background_label.place(relwidth=1, relheight=1)

    for i in range(5):
        tk.Label(updates_window, text=f"Classic Label {i}").place(x=50, y=130 + 50 * i)


def open_url(event, url: str) -> None:
    """
    Opens a URL in the default web browser when triggered by an event, such as a button click.

    ### Parameters
    - `event`: The event object triggering the function (e.g., a button click event).
    - `url` (str): The URL to be opened in the default web browser.

    ### Returns
    This function does not return any value (`None`).

    ### Dependencies
    - `open_new_tab(url)`: This function is part of the `webbrowser` module and is used to open the specified URL in a new browser tab.

    ### Example
    ```python
    from webbrowser import open_new_tab

    # ...

    url = "https://example.com"
    open_url(event, url)

    """
    open_new_tab(url)


def launch_visual() -> None:
    """Handles the launch button click event."""
    result = messagebox.askyesno("Launch App", "Do you want to start monitoring...")
    if result:
        pass


def launch_stat() -> None:
    """Handles the launch stat event."""
    result = messagebox.askyesno("Launching Stat", "Do you want to start monitoring...")
    if result:
        pass


def load_urls_from_config(file_path: str) -> dict[str:str]:
    """
    This function loads URLs from a JSON configuration file and returns them as a dictionary.

    ### Parameters
    - `file_path: str`:- The file path to the configuration file containing URLs.

    ### Returns
    - `urls: dict`:- A dictionary containing key-value pairs of URL names and their corresponding addresses.

    ### Raises
    - `FileNotFoundError`: If the specified configuration file is not found.
    - `json.JSONDecodeError`: If the configuration file is not a valid JSON format.

    ### Example
    ```python
    file_path = "config.json"
    urls = load_urls_from_config(file_path)
    print(urls)

    """
    with open(file_path, "r") as config_file:
        urls = json.load(config_file)
        return urls


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    logging.warning(
        "This is a utility module for the GUI of the software. Do not run this as a script."
    )
