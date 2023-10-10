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
This module contains utilitis for view module for the MCV Design pattern followed by the project.
Do not run this as a script.

:Metadata::
:author: Aviraj Saha
:date: 2023-10-08 | YYYY-MM-DD
:purpose: Utility for GUI.
"""


# Imports
from lazy_import import lazy_function, lazy_module
from tkinter import messagebox

# Lazy Imports
open_new_tab = lazy_function("webbrowser", "open_new_tab")
logging = lazy_module("logging")


# Utility functions for GUI.
def search_for_updates() -> None:
    """Handles the search for updates button click event."""
    messagebox.showinfo("Search for Updates", "Checking for updates...")


def open_url(event, url) -> None:
    """Opens a URL in the default web browser."""
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


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    logging.warning(
        "This is a utility module for the GUI of the software. Do not run this as a script."
    )
