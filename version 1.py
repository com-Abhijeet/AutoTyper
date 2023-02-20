import pyautogui
import time
import tkinter as tk
from tkinter import filedialog
import os

class MainWindow:

    def __init__(self, master):
        self.master = master
        master.title("Autotype Essay")
        master.geometry("600x400")

        # Create a frame to hold the input widgets.
        input_frame = tk.Frame(master)
        input_frame.pack(pady=20)

        # Create a label and text box for the input.
        self.input_label = tk.Label(input_frame, text="Input:")
        self.input_label.pack(side=tk.LEFT, padx=10)

        self.text_input = tk.Text(input_frame, height=10, width=50)
        self.text_input.pack(side=tk.LEFT)

        # If "last_input.txt" exists, read the last input and insert it into the text box.
        if os.path.isfile("last_input.txt"):
            with open("last_input.txt", "r") as f:
                last_input = f.read()
                self.text_input.insert(tk.END, last_input)

        # Create a frame to hold the radio buttons.
        radio_frame = tk.Frame(master)
        radio_frame.pack()

        # Create radio buttons for selecting input source.
        self.var = tk.StringVar(value="file")
        self.radio_button_1 = tk.Radiobutton(radio_frame, text="Autotype from File", variable=self.var, value="file", command=self.select_file)
        self.radio_button_2 = tk.Radiobutton(radio_frame, text="Autotype from Text", variable=self.var, value="text")
        self.radio_button_1.pack(side=tk.LEFT, padx=10)
        self.radio_button_2.pack(side=tk.LEFT)

        # Create a frame to hold the delay input.
        delay_frame = tk.Frame(master)
        delay_frame.pack(pady=10)

        # Create a label and entry box for the delay.
        self.time_label = tk.Label(delay_frame, text="Delay (in seconds):")
        self.time_label.pack(side=tk.LEFT, padx=10)

        self.time_input = tk.Entry(delay_frame, width=10)
        self.time_input.insert(0, "10")
        self.time_input.pack(side=tk.LEFT)

        # Create a button to start the autotyping.
        self.run_button = tk.Button(master, text="Start", command=self.run_autotype)
        self.run_button.pack(pady=10)

        # Initialize the file path to None.
        self.file_path = None

    def select_file(self):
        # If "Autotype from File" is selected, ask the user to select a file immediately.
        if self.var.get() == "file":
            self.file_path = filedialog.askopenfilename(title="Select file", filetypes=[("Text files", "*.txt")])
            self.text_input.delete("1.0", tk.END)

            with open(self.file_path, "r") as f:
                essay = f.read()
                self.text_input.insert(tk.END, essay)

    def run_autotype(self):
        delay = int(self.time_input.get())
        if self.var.get() == "file":
            # If "Autotype from File" is selected, use the selected file path.
            with open(self.file_path, "r") as f:
                essay = f.read()
        else:
            essay = self.text_input.get("1.0", tk.END)

        # Save the current input to "last_input.txt".
        with open("last_input.txt", "w") as f:
            f.write(essay)

        time.sleep(delay)
        pyautogui.typewrite(essay)

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
