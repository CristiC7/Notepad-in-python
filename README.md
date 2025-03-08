# Notepad-in-python
This program implements a simple Notepad application using Python's Tkinter library to create a graphical user interface. This application allows the user to write, edit, open and save text files.

Functionalities of the application:

◆ Creating a main window:


The Notepad class inherits tk.Tk and creates the main application window.

Set the window title (self.title("Notepad")).

Create a Text widget (self.text) where the user can enter and edit text.


◆ Creating a navigation menu:


• Add a File menu with options:

New - creates a new document (deletes the current text).

Open - opens an existing text file.

Save - saves the current content to a file.

Exit - closes the application.

• Add an Edit menu with options:

Cut - cuts the selected text.

Copy - copies the selected text.

Paste - inserts the copied text.

◆ Main application functions:

new_file(): deletes the current text and resets the window title.

open_file(): opens a dialog box for selecting a text file, then displays its contents in the editor.

save_file(): saves the current text to a user-selected file.

cut(), copy(), paste(): use Tkinter's default functionality for editing operations.

◆ Initializing and running the application:

if __name__ == "__main__": ensure that the application only runs when the file is executed directly.

notepad = Notepad() creates the application instance.

notepad.mainloop() starts the main Tkinter loop to keep the window active.
