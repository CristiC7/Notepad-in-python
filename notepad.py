import tkinter as tk  # Import the Tkinter library for GUI functionality
from tkinter import filedialog  # Import filedialog for file operations

class Notepad(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Set the title for the Notepad application
        self.title("Notepad")

        # Create a text widget where users can type
        self.text = tk.Text(self, wrap="word")  # Enable word wrapping
        self.text.pack(side="top", fill="both", expand=True)  # Expand the text area to fill the window

        # Create a menu bar
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        # Create a "File" menu with options to create, open, save, and exit
        file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=file_menu)  # Add "File" to the menu bar
        file_menu.add_command(label="New", command=self.new_file)  # Create a new file
        file_menu.add_command(label="Open", command=self.open_file)  # Open an existing file
        file_menu.add_command(label="Save", command=self.save_file)  # Save the current file
        file_menu.add_separator()  # Add a separator line
        file_menu.add_command(label="Exit", command=self.quit)  # Exit the application

        # Create an "Edit" menu with options for cut, copy, and paste
        edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=edit_menu)  # Add "Edit" to the menu bar
        edit_menu.add_command(label="Cut", command=self.cut)  # Cut selected text
        edit_menu.add_command(label="Copy", command=self.copy)  # Copy selected text
        edit_menu.add_command(label="Paste", command=self.paste)  # Paste copied text

    # Function to create a new file (clears the text area)
    def new_file(self):
        self.text.delete("1.0", "end")  # Delete all text in the editor
        self.title("Notepad")  # Reset the window title

    # Function to open a file and display its contents in the text editor
    def open_file(self):
        file = filedialog.askopenfile(parent=self, mode="rb", title="Open a file")  # Open file dialog
        if file:
            contents = file.read()  # Read the file contents
            self.text.delete("1.0", "end")  # Clear the current text
            self.text.insert("1.0", contents)  # Insert file content into text editor
            file.close()  # Close the file
            self.title(file.name + " - Notepad")  # Update the window title

    # Function to save the current text to a file
    def save_file(self):
        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", 
                                        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])  # Save file dialog
        if file:
            contents = self.text.get("1.0", "end")  # Get all text from the editor
            file.write(contents)  # Write text to the file
            file.close()  # Close the file
            self.title(file.name + " - Notepad")  # Update the window title

    # Function to cut the selected text
    def cut(self):
        self.text.event_generate("<<Cut>>")  # Perform cut operation

    # Function to copy the selected text
    def copy(self):
        self.text.event_generate("<<Copy>>")  # Perform copy operation

    # Function to paste text from clipboard
    def paste(self):
        self.text.event_generate("<<Paste>>")  # Perform paste operation

# Create and run the Notepad application
if __name__ == "__main__":
    notepad = Notepad()  # Initialize the Notepad app
    notepad.mainloop()  # Run the Tkinter event loop
