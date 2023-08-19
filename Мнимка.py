import tkinter as tk
import subprocess
import os
import http.client

def send_message():
    user_input = input_entry.get()
    chat_text.insert(tk.END, "Вы: " + user_input + "\n")
    
    if user_input.startswith("команда:"):
        command = user_input.replace("команда:", "").strip()
        try:
            result = subprocess.check_output(command, shell=True, text=True)
            chat_text.insert(tk.END, "Мнимка: Результат выполнения команды:\n" + result + "\n")
        except subprocess.CalledProcessError as e:
            chat_text.insert(tk.END, "Мнимка: Ошибка выполнения команды: " + str(e) + "\n")
    elif user_input.startswith("файл:"):
        file_path = user_input.replace("файл:", "").strip()
        try:
            with open(file_path, "r") as file:
                code = file.read()
            exec(code)
            chat_text.insert(tk.END, "Мнимка: Файл успешно выполнен!\n")
        except FileNotFoundError:
            chat_text.insert(tk.END, "Мнимка: Файл не найден!\n")
        except Exception as e:
            chat_text.insert(tk.END, "Мнимка: Ошибка выполнения файла: " + str(e) + "\n")
    elif user_input.startswith("пример:"):
        example = user_input.replace("пример:", "").strip()
        try:
            result = eval(example)
            chat_text.insert(tk.END, "Мнимка: Результат примера: " + str(result) + "\n")
        except Exception as e:
            chat_text.insert(tk.END, "Мнимка: Ошибка выполнения примера: " + str(e) + "\n")
    elif user_input.startswith("интернет:"):
        url = user_input.replace("интернет:", "").strip()
        try:
            conn = http.client.HTTPSConnection(url)
            conn.request("GET", "/")
            response = conn.getresponse()
            chat_text.insert(tk.END, "Мнимка: Запрос выполнен успешно!\n")
            # здесь можно добавить логику для обработки ответа от сервера
        except Exception as e:
            chat_text.insert(tk.END, "Мнимка: Ошибка выполнения запроса: " + str(e) + "\n")
    elif user_input.startswith("компьютер:"):
        computer_command = user_input.replace("компьютер:", "").strip()
        try:
            output = os.popen(computer_command).read()
            chat_text.insert(tk.END, "Мнимка: Результат выполнения команды компьютера:\n" + output + "\n")
        except Exception as e:
            chat_text.insert(tk.END, "Мнимка: Ошибка выполнения команды компьютера: " + str(e) + "\n")
    else:
        chat_text.insert(tk.END, "Мнимка: Я не понимаю, попробуйте другую команду!\n")
    
    input_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Чат с Мнимкой")

chat_text = tk.Text(root, height=10, width=50)
chat_text.pack()

input_entry = tk.Entry(root, width=50)
input_entry.pack()

send_button = tk.Button(root, text="Отправить", command=send_message)
send_button.pack()

root.mainloop()