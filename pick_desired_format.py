#!/usr/bin/env python3
"""
prompts user to select a choice
returns selected choice
"""

import tkinter as tk


# Create a hidden root window
root = tk.Tk()
# assign icon
root.iconbitmap(default='./icon/icon.ico')
# Hide the main tkinter window
root.withdraw()

# Function to display a custom dialog box with three options
def pick_format(box_title="Format selection",
                    box_text = "Format to convert\nmedia INTO"):
    # list of output formats
    opt1=".m4a"
    opt1_desc="placeholder tooltip"
    opt2=".mp3"
    opt3=".WAV"
    opt4=".ogg"

    # Create a new top-level window for the dialog
    dialog = tk.Toplevel(root)
    dialog.title(box_title)
    dialog.geometry("225x300")
    dialog.resizable(False, False)

    # Variable to store the user's choice
    user_choice = tk.StringVar(value="Cancel")  # Default to "Cancel"

    # Label with the message
    tk.Label(dialog, text=box_text).pack(side="top", pady=25)

    # Buttons for the options
    def select_option(option):
        user_choice.set(option)
        dialog.destroy()  # Close the dialog

    # button_mp3 = tk.Button(dialog, text=opt1, command=lambda: select_option(opt1)).pack(side="top")
    tk.Button(dialog, text=opt1, command=lambda: select_option(opt1)).pack(side="top")
    tk.Button(dialog, text=opt2, command=lambda: select_option(opt2)).pack(side="top")
    tk.Button(dialog, text=opt3, command=lambda: select_option(opt3)).pack(side="top")
    tk.Button(dialog, text=opt4, command=lambda: select_option(opt4)).pack(side="top")
    tk.Button(dialog, text="Cancel", command=lambda: select_option("cancel")).pack(side="bottom",padx=1, pady=15)

    # Wait for the user to make a selection
    dialog.wait_window()

    return user_choice.get()


if __name__ == '__main__':
    # Call the function and store the result
    selected_option = pick_format()
    print(f"You selected: {selected_option}")
