import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import os
import datetime

class CleaningRobotTestAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Cleaning Robot Automation Test Assistant")

        # Welcome text
        self.welcome_label = tk.Label(root, text="Hello, I am your cleaning robot automation test assistant.", font=('Arial', 16))
        self.welcome_label.pack(pady=20)

        # Load script button
        self.load_script_button = tk.Button(root, text="Load Test Script", command=self.load_script)
        self.load_script_button.pack(pady=10)

        # Script input area
        self.script_text = scrolledtext.ScrolledText(root, height=10, width=50, state='disabled')
        self.script_text.pack()

        # Start Test button
        self.start_test_button = tk.Button(root, text="Start Test", command=self.start_test)
        self.start_test_button.pack(pady=20)

        # Test result display area
        self.result_label = tk.Label(root, text="Test Results:")
        self.result_label.pack(pady=(10, 0))
        self.result_text = scrolledtext.ScrolledText(root, height=10, width=50)
        self.result_text.pack()

        # Save Test Result button
        self.save_result_button = tk.Button(root, text="Save Test Result", command=self.save_result)
        self.save_result_button.pack(pady=20)

    def load_script(self):
        # Open a dialog to choose the script file
        file_path = filedialog.askopenfilename(
            title="Select Test Script",
            filetypes=[("Text files", "*.py"), ("All files", "*.*")]
        )
        if file_path:
            self.script_text.config(state='normal')
            self.script_text.delete(1.0, tk.END)
            with open(file_path, 'r') as file:
                self.script_text.insert(tk.END, file.read())
            self.script_text.config(state='disabled')

    def start_test(self):
        # Simulate a test result
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.current_time = datetime.datetime.now().isoformat()
        self.result_text.insert(tk.END, f"{self.current_time}: Test started...\n")
        self.current_time = datetime.datetime.now().isoformat()
        self.result_text.insert(tk.END, f"{self.current_time}: Test completed successfully.\n")
        self.result_text.config(state='disabled')

    def save_result(self):
        # Open a dialog to choose the result file path
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                  filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            # Write the content of the result_text to the file
            with open(file_path, 'w') as file:
                file.write(self.result_text.get(1.0, tk.END))
            self.root.title("Test Result Saved - Cleaning Robot Automation Test Assistant")

# Create the main window and pass it to the GUI application
root = tk.Tk()
app = CleaningRobotTestAssistant(root)
root.mainloop()