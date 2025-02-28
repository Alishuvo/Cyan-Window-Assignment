import tkinter as tk

# Function to close window when 'S' key is pressed
def on_keypress(event):
    if event.char.lower() == 's':
        root.destroy()

# Create main window
root = tk.Tk()
root.title("Shahanawas Ali Shuvo")  # Setting window title
root.configure(bg='cyan')  # Setting background color
root.geometry("400x300")  # Setting window size

# Bind keypress event
root.bind("<KeyPress>", on_keypress)

# Run the application
root.mainloop()
