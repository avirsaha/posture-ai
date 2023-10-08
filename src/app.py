import tkinter as tk
from tkinter import messagebox
# from PIL import Image, ImageTk
import main


# Function to handle the search for updates button click event
def search_for_updates():
    messagebox.showinfo("Search for Updates", "Checking for updates...")


# Function to handle the launch button click event
def launch_app():
    result = messagebox.askyesno("Launch App", "Do you want to start monitoring...")
    if result:
        main.main()


# Function to change button color on hover
def on_hover(event):
    update_button.config(bg="yellow", fg="black")


# Function to change button color back to black when not hovered
def on_leave(event):
    update_button.config(bg="black", fg="white")


# Creating the main window
root = tk.Tk()
root.title("Sitfix-ai")

# Setting window size
root.geometry("1025x765")
root.resizable(False, False)

# Set the window icon
# root.iconbitmap("imgs/sitfixlogo.ico")  # Specify the path to your icon file

# Load the background image
# background_image = Image.open("imgs/Sitfix-ai-home.png")
# background_photo = ImageTk.PhotoImage(background_image)

# # Create a label with the background image
# background_label = tk.Label(root, image=background_photo)
# background_label.image = background_photo
# background_label.place(relwidth=1, relheight=1)

# Creating and placing the search for updates button (initially black)
update_button = tk.Button(
    root,
    text="Search for Updates",
    command=search_for_updates,
    width=20,
    bg="black",
    fg="white",
)
update_button.place(x=660, y=190)

# Creating and placing the launch button
launch_button = tk.Button(
    root, text="Launch", command=launch_app, width=20, bg="Yellow", fg="black"
)
launch_button.place(x=660, y=400)

# Binding hover and leave events to the update button
update_button.bind("<Enter>", on_hover)
update_button.bind("<Leave>", on_leave)

# Running the Tkinter main loop
root.mainloop()
