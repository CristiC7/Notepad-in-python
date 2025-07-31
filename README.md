# 📝 Notepad in Python with Tkinter

This project is a simple **Notepad-style text editor** built using **Python's Tkinter** library.  
It provides essential file editing features such as writing, saving, opening, and editing text files, all within a graphical user interface (GUI).

---

## ✅ Features

### 📁 File Menu
- **New** – Clears the text area and resets the window title
- **Open** – Opens a `.txt` file using a file dialog and loads its content
- **Save** – Saves the current text to a selected file (default `.txt`)
- **Exit** – Closes the application

### ✂️ Edit Menu
- **Cut** – Cuts the selected text
- **Copy** – Copies the selected text
- **Paste** – Pastes the clipboard content into the editor

### 🖥️ Interface
- GUI created using Tkinter's `Text` widget
- Word wrapping enabled for easier reading
- Dynamically resizable window
- Built-in `filedialog` for file I/O

---

## 🔧 How It Works

- The main class `Notepad` inherits from `tk.Tk`, creating the root window.
- The text editing area is implemented using `Text()`.
- Menus (`File`, `Edit`) are created using `Menu()` and added to the top menu bar.
- Core methods:
  - `new_file()` – Clears all text from the editor
  - `open_file()` – Opens a file and displays its content
  - `save_file()` – Saves current content to a file
  - `cut()`, `copy()`, `paste()` – Use built-in event generation for editing

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Save the file as `notepad.py`.
3. Run the file:

```bash
python notepad.py
```

---

## 🖱️ GUI Overview
- Text Area: Main writing panel with scroll and word-wrap

- File Menu:

  - New: Clears the text area

  - Open: Loads content from an existing file

  - Save: Saves content to a file (with extension .txt by default)

  - Exit: Closes the application

- Edit Menu:

  - Cut: Removes and copies selected text

  - Copy: Copies selected text

  - Paste: Pastes copied text into the cursor position

---

## 💡 Potential Improvements
- Add font selection or theme options (dark/light mode)

- Add keyboard shortcuts (Ctrl+S, Ctrl+O, etc.)

- Add status bar (line number, word count)

- Implement undo/redo functionality

---

## 👨‍💻 Author
Created by CristiC7

Beginner-friendly text editor built using Python and Tkinter.

Open to improvements and contributions!
