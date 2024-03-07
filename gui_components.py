import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from threading import Thread


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
    def __init__(self, parent, start_automation_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.choose_data_label = tk.Label(self, text="Choose your data set", anchor="w")
        self.choose_data_label.pack(side=tk.LEFT, fill='x')
        self.column_selector = ttk.Combobox(self, state="readonly")
        self.column_selector.pack(side=tk.LEFT, padx=(10, 10))
        self.automation_button = tk.Button(self, text="Start Automation", command=start_automation_callback)
        self.automation_button.pack(side=tk.LEFT)
        self.set_state(tk.DISABLED)
        self.create_cancel_button_window()

    def create_cancel_button_window(self):
        self.cancel_window = tk.Toplevel(self)
        self.cancel_window.overrideredirect(True)
        self.cancel_window.geometry("500x50")
        self.cancel_window.attributes("-topmost", True)

        button_font = Font(family="Helvetica", size=24, weight="bold")
        cancel_button = tk.Button(
            self.cancel_window,
            text="CANCEL",
            command=self.cancel_automation,
            font=button_font,
            bg="#90EE90")
        cancel_button.pack(expand=True, fill=tk.BOTH)

    def cancel_automation(self):
        global automation_thread
        automation_thread = False
        print("Cancel Automation: {}".format(automation_thread))

    def set_state(self, state):
        for child in self.winfo_children():
            if isinstance(child, (ttk.Combobox, tk.Button)):
                child.configure(state=state)

    def set_data_series(self, data_series):
        self.data_series = data_series
        column_names = ["Pon-Sob", "Pon-Czw", "Wt-Czw", "Sr-Pt", "Wt-Sob"]
        self.column_selector['values'] = \
            column_names if column_names else [f"Column {i + 1}" for i in range(len(self.data_series))]
