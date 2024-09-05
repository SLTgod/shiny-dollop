from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

# Создаем главное окно приложения
root = Tk()

# Функция для генерации QR-кода
def generate():
    # Получаем данные из полей ввода
    link_name = name_entry.get()  # Название ссылки (имя файла)
    link = link_entry.get()  # Ссылка (текст для кодирования)

    # Формируем имя файла для сохранения QR-кода
    file_name = link_name + ".png"

    # Создаем QR-код с помощью pyqrcode
    url = pyqrcode.create(link)

    # Сохраняем QR-код в виде PNG-файла
    url.png(file_name, scale=8)

    # Открываем сохраненный файл и отображаем изображение в интерфейсе
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image  # Сохраняем ссылку на изображение, чтобы не удалилось
    canvas.create_window(200, 450, window=image_label)


# Создаем холст для размещения элементов интерфейса
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# Добавляем заголовок приложения
app_label = Label(root, text="Генератор QR-кода", fg="blue", font=("Arial", 30))
canvas.create_window(200, 50, window=app_label)

# Добавляем метки для полей ввода
name_label = Label(root, text='Название ссылки')
link_label = Label(root, text='Ссылка')
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

# Поля для ввода текста (имя файла и ссылка для кодирования)
name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

# Кнопка для генерации QR-кода
button = Button(text="Создать QR-код", command=generate)
canvas.create_window(200, 230, window=button)

# Запускаем главный цикл приложения
root.mainloop()