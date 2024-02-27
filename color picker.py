import tkinter as tk
from tkinter import colorchooser

def pick_color():
    color_code, color_name = colorchooser.askcolor(title="Pick a Color")
    color_label.config(text=f"Selected Color: {color_name}")
    color_display.config(bg=color_code)

# Create the main window
root = tk.Tk()
root.title("Color Picker")

# Create a button to trigger the color picker
pick_button = tk.Button(root, text="Pick a Color", command=pick_color)
pick_button.pack(pady=10)

# Create a label to display the selected color
color_label = tk.Label(root, text="Selected Color: None")
color_label.pack()

# Create a canvas to display the selected color
color_display = tk.Canvas(root, width=50, height=50, bg="white")
color_display.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
