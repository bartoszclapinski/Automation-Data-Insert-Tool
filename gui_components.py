import tkinter as tk
from tkinter import ttk


class FileLoadFrame(tk.Frame):
    def __init__(self, parent, load_callback):
        super().__init__(parent)
        self.load_button = tk.Button(self, text="Load Excel File", command=load_callback)
        self.load_button.pack(side=tk.LEFT, padx=(0, 10))
        self.file_name_label = tk.Label(self, text="None", anchor="w")
        self.file_name_label.pack(side=tk.LEFT, fill='x', expand=True)

    def set_file_name(self, file_name):
        self.file_name_label.config(text=file_name)


class AutomationFrame(tk.Frame):
    def __init__(self, parent, start_automation_callback):
        super().__init__(parent)
        self.choose_data_label = tk.Label(self, text="Choose your data set", anchor="w")
        self.choose_data_label.pack(side=tk.LEFT, fill='x')
        self.column_selector = ttk.Combobox(self, state="readonly")
        self.column_selector.pack(side=tk.LEFT, padx=(10, 10))
        self.automation_button = tk.Button(self, text="Start Automation", command=start_automation_callback)
        self.automation_button.pack(side=tk.LEFT)
        self.set_state(tk.DISABLED)

    def set_state(self, state):
        for child in self.winfo_children():
            child.configure(state=state)

    def set_data_series(self, data_series):
        self.data_series = data_series
        column_names = ["Pon-Sob", "Pon-Czw", "Wt-Czw", "Sr-Pt", "Wt-Sob"]
        self.column_selector['values'] = \
            column_names if column_names else [f"Column {i + 1}" for i in range(len(self.data_series))]

