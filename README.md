 <div align="center">

# ✍️ Undo–Redo Text Editor Using Stack

### A Python GUI Application Demonstrating Stack-Based Text History

A simple, interactive text editor built with **Python** and **Tkinter**, demonstrating how two stacks implement Undo and Redo operations.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-Tkinter-2E8B57?style=for-the-badge)
![DSA](https://img.shields.io/badge/Topic-Data%20Structures-orange?style=for-the-badge)
![Project](https://img.shields.io/badge/Project-College%20Microproject-6C63FF?style=for-the-badge)

</div>

---

## 📌 About the Project

The **Undo–Redo Text Editor Using Stack** is a Data Structures and Algorithms (DSA) microproject developed using Python. It provides a graphical interface where users can add text, undo the latest change, redo an undone change, clear the text, and open or save text files.

The project uses two stacks to maintain text history:

- **Undo Stack:** Stores previous text states.
- **Redo Stack:** Stores text states that can be restored after an Undo operation.

This project demonstrates the **LIFO (Last In, First Out)** principle through a practical application.

## ✨ Features

- ➕ **Add Text** — add text using the input field.
- ↩️ **Undo** — restore the previous text state.
- ↪️ **Redo** — restore an undone text state.
- 🧹 **Clear Text** — clear the current text while keeping the operation undoable.
- 📂 **Open File** — load text from a `.txt` file.
- 💾 **Save File** — save the current text to a `.txt` file.
- 🔢 **Character Counter** — display the current character count.
- 🪟 **Graphical User Interface** — interact through a Tkinter window.
- ℹ️ **About Dialog** — display project information.

## 🧠 Data Structures and Algorithms

### Stack

A stack is a linear data structure that follows the **LIFO (Last In, First Out)** principle. The last item added is the first item removed.

Python lists support stack operations through `append()` and `pop()`.

```python
stack.append(item)  # Push an item onto the stack
item = stack.pop()  # Pop the top item
```

### How Undo and Redo Work

| Operation | Description |
|---|---|
| Add Text | Saves the current text in the Undo Stack, adds new text, and clears redo history. |
| Undo | Saves the current text in the Redo Stack and restores the previous state. |
| Redo | Saves the current text in the Undo Stack and restores the undone state. |
| Clear Text | Saves the current state before clearing the text. |
| Open File | Loads a text file and preserves the previous state for Undo. |

**Note:** This project stores complete text snapshots rather than individual keystrokes. Text is entered through the input field, and the main editor area displays the current text.

## 🖥️ Application Preview

The application window includes:

- A project title and header.
- A text input field and Add Text button.
- Undo, Redo, Clear Text, Open File, and Save File buttons.
- A scrollable text display area.
- A status bar showing the character count.

To display a screenshot, save an image of the running application as `assets/screenshot.png` and add the following Markdown:

```markdown
![Application Screenshot](assets/screenshot.png)
```

## 🛠️ Technologies Used

- **Python 3** — application logic.
- **Tkinter** — graphical user interface.
- **Python Lists** — implementation of the Undo and Redo stacks.

Tkinter is included with most standard Python installations. No third-party Python packages are required for the application code.

## 📁 Project Structure

```text
undo-redo-text-editor/
│
├── undo_redo_text_editor_gui.py
├── README.md

```

The `assets` folder is optional and can be used to store screenshots of the application.

## 🚀 Installation and Execution

### Prerequisites

- Python 3 installed on your computer.
- VS Code, IDLE, or another Python editor.

Check your Python installation:

```bash
python --version
```

On Windows, you can also use:

```bash
py --version
```

### Clone the Repository

Replace `YOUR-USERNAME` with your GitHub username and use your actual repository name.

```bash
git clone https://github.com/YOUR-USERNAME/undo-redo-text-editor.git
```

Navigate to the project folder:

```bash
cd undo-redo-text-editor
```

### Run the Application

```bash
python undo_redo_text_editor_gui.py
```

On Windows, if required:

```bash
py undo_redo_text_editor_gui.py
```

The GUI window should open, allowing you to test the text editor.

### If Tkinter Is Missing

Most standard Python installations include Tkinter. If it is unavailable, install or repair the Tk/Tcl component for your Python distribution.

On Debian or Ubuntu Linux, use:

```bash
sudo apt install python3-tk
```

## 🧪 Example Workflow

1. Enter `Hello` in the input field and click **Add Text**.
2. Enter `World` and click **Add Text** again.
3. The current text becomes `Hello World`.
4. Click **Undo** to restore `Hello`.
5. Click **Redo** to restore `Hello World`.
6. Click **Save File** to save the current text.

## ⏱️ Time Complexity

Let `n` represent the current text length and `m` represent the length of the newly added text.

| Operation | Approximate Time Complexity |
|---|---|
| Stack `append()` / `pop()` | `O(1)` on average |
| Add Text | `O(n + m)` |
| Undo | `O(n)` |
| Redo | `O(n)` |

Because the program stores complete text snapshots, memory usage increases as more text states are saved.

## 🎓 Academic Project Details

**Project Title:** Undo–Redo Text Editor Using Stack in Python

**Course:** 25DC301 – Data Structures and Algorithms

**Institution:** Karunya Institute of Technology and Sciences

**Department:** Artificial Intelligence and Data Science

**Course Faculty / Supervisor:** Dr. K. Vidhiya

### 👥 Team Members

| Name | Register Number |
|---|---|
| Dharani Dharan M | URK25AI1043 |
| Robinson A | URK25AI1006 |
| Joe Flamming M | URK25AI1004 |
| Lithish Kumar P | URK25AI1027 |

## 🔮 Future Enhancements

- Add character-level editing and cursor positioning.
- Implement keyboard shortcuts for Undo and Redo.
- Limit history size to manage memory usage.
- Add additional text-editing tools.
- Store individual editing actions instead of complete text snapshots.

## 🤝 Contributing

This is a college learning project. Suggestions and improvements are welcome.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test the application.
5. Submit a pull request describing your improvements.

## 📄 License

This project is intended for educational use. Before distributing it publicly, add a `LICENSE` file specifying the permissions and conditions for reuse.

---

<div align="center">

**Built with Python 🐍**

*Learning Data Structures by building something practical.*

</div>
