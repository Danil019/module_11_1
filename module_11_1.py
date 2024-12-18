from time import sleep

import requests
import matplotlib.pyplot as plt
from PIL import Image
import time


# 1-я библиотека. Запросы
print('Запрос погоды в Сочи, на ближайшие три дня')
time.sleep(1)
url = 'https://wttr.in/Sochi'
result = requests.get(url) # делаем запрос
if result.status_code == 200: # если успешен, то выводим статус
    print('Запрос успешно выполнен, и сервер вернул результат', result.status_code)
print(result.text) #
print('Encoding:', '-->', result.encoding, '<--\n')
print(result.headers['Date'])

print('\nПереход ко 2-ой библиотеке. "Визуализирование данных"')
time.sleep(2)
print('\nГрафик построен, ожидайте')
time.sleep(1)


# 2-я библиотека для построения графиков
# Линейный график
x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 1, 6]

plt.plot(x, y, label='Тестовый график') # рисует график и отображение легенды(точнее название, за отображение отвечает plt.legend())
plt.ylabel('Ось Y')
plt.xlabel('Ось X')
plt.title('Мой график')
plt.legend()
plt.grid(True) # отображение сетки
plt.show() # показать график
plt.savefig('graph.png') # сохранить график в файле png, можно и в pdf

print('Построение гистограммы')
time.sleep(2)

# Гистограмма
data = [1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6, 6, 7]
# Гистограмма с 5 корзинами, вроде так называется. То есть широкие интервалы
plt.hist(data, bins=5)
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.title("Гистограмма")
plt.show()
# Гистограмма с 10 корзинами
plt.hist(data, bins=10)
plt.title("Гистограмма с 10 корзинами")
plt.show()

print('Переход к следующей библиотеке. "Редактор изображений"')
time.sleep(2)

# 3-я библиотека. "Редактор изображений"

print('Изображение открывается и преображается')
# открываем изображение
image = Image.open('simple_picture.png')
# Поворот изображения
rotate_image = image.rotate(180)
# Преобразование в RGB (удаляет альфа-канал). Формат JPEG не поддерживает альфа-канал, поэтому Pillow не может
# сохранить изображение с этим режимом в формат JPEG.
rotate_image_rgb = rotate_image.convert('RGB')
# изменение разрешения изображения
image_resized = rotate_image_rgb.resize((600, 600))
# Сохранение в другом формате
image_resized.save('image_resized.jpg')

time.sleep(1)
print('Изображение изменено')