import tkinter as tk
from tkinter import filedialog, messagebox
import threading
from excel_reader import read_excel_all_columns
from automation import automate_keyboard_actions, automate_test
from gui_components import FileLoadFrame, AutomationFrame
from generator import save_to_excel, generate_data_for_day_pairs


class ExcelDataReaderGUI:
    def __init__(self, window):
        self.file_path = None
        self.columns_data = None

        self.window = window
        window.title("Automation Data Insert")

        # Center the window
        self.center_window()

        # Load file Section
        self.file_load_frame = FileLoadFrame(window, self.load_file)
        self.file_load_frame.pack(padx=10, pady=10, fill='x')

        # Automation Section
        self.automation_frame = AutomationFrame(window, self.start_automation)
        self.automation_frame.pack(padx=10, pady=10, fill='x')
        self.automation_frame.set_state(tk.DISABLED)

        # Data Generator Section
        data_generator_frame = tk.Frame(window)
        data_generator_frame.pack(padx=10, pady=10, fill='x')
        data_generator_button = tk.Button(data_generator_frame, text="Generate Data", command=self.generate_data)
        data_generator_button.pack(side=tk.LEFT, padx=(0, 10))

        # Text Area Section
        frame = tk.Frame(window)
        frame.pack(padx=10, pady=10)
        self.text_area = tk.Text(window, height=15, width=50)
        self.text_area.pack(padx=10, pady=10)

    def center_window(self, w=800, h=800):
        # get screen width and height
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            self.file_path = file_path
            columns_data = read_excel_all_columns(file_path)
            self.columns_data = columns_data
            # Update file label
            self.file_load_frame.set_file_name(file_path)
            # Populate the ComboBox with column indices
            self.automation_frame.set_data_series(columns_data)
            self.automation_frame.set_state(tk.NORMAL)
        else:
            self.file_load_frame.set_file_name("None")
            self.automation_frame.set_state(tk.DISABLED)

    def start_automation(self):
        selected_index = self.automation_frame.column_selector.current()
        if selected_index is not None:
            selected_data = self.columns_data[selected_index]
            automation_thread = threading.Thread(
                target=automate_test,
                args=(selected_data, self.update_text_area))
            automation_thread.start()
        else:
            messagebox.showerror("Error", "Data not loaded. Please load an Excel file first.")

    def update_text_area(self, text):
        self.text_area.insert(tk.END, text)
        self.text_area.see(tk.END)

    @staticmethod
    def generate_data():
        try:
            year = 2024
            month = 1
            day_pairs = [(0, 5), (0, 3), (1, 3), (2, 4), (1, 5)]
            generated_pairs = generate_data_for_day_pairs(year, month, day_pairs)
            save_to_excel(generated_pairs, f"F:\\Repos\\Python-Projects\\DataFiles\\output-{month}-{year}.xlsx")
            messagebox.showinfo("Success", "Data generated successfully")

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelDataReaderGUI(root)
    root.mainloop()
