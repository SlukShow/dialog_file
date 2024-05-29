import tkinter as tk
from tkinter import filedialog

def choose_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        label.config(text="Вибраний файл: " + file_path)
        analyze_text(file_path)

def analyze_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_in_file = file.read()
            words = text_in_file.split()
            word_count = len(words)
            char_count = len(text_in_file)
            result_text = f"Кількість слів: {word_count}, Кількість символів: {char_count}"
            result_label.config(text=result_text)
    except Exception as e:
        result_label.config(text=f"Помилка: {e}")

root = tk.Tk()
root.title("Оберіть файл")
width = 300
height = 150
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

label = tk.Label(root, text="")
label.pack(pady=5)

button = tk.Button(root, text="Обрати файл", command=choose_file)
button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
