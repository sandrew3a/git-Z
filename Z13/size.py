# модуль импорта
import os

# Сканируем каждый файл в папке с помощью os.scandir().
# Метод os.stat() возвращает свойства файла,
# с помощью os.stat().st_size вычисляем размер файла.
# Таким образом, можно вычислить общий размер папки.

def get_size(path):
    size = 0
# получить размер
    if os.path.isfile(path):
        size = os.path.getsize(path)
    else:
        for ele in os.scandir(path):
            size += os.stat(ele).st_size
    return size

# Чтобы результат был удобно воспринимаемым, изменяем представление данных о размере файлов:
def human_readable_size(size):
#    # Конвертируем байты в более удобные для восприятия единицы измерения
    for unit in [' байт', ' КБ', ' МБ', ' ГБ', ' ТБ', ' ПБ']:
        if size < 1024:
            break
        size /= 1024
    return f"{size:7.2f}{unit}"


# Функция main() упрощает управление потоком программы и позволяет добавить больше логики в структуру программ

def main():
# Текущий рабочий каталог
  pwd = os.getcwd()
# Список имён всех файлов и каталогов в указанном пути
  items = os.listdir(pwd)
# Создаём пустой список
  size_list = []
  for item in items:
# Объединение одного или нескольких путей к файлам и каталогам
    full_path = os.path.join(pwd, item)
# Вычсление размера файла или апки
    size = get_size(full_path)
# Заполнение списка
    size_list.append((size, item))
# Сортировка списка в убывающем порядке по первому элементу
  size_list.sort(key=lambda x: x[0], reverse=True)

  for size, item in size_list:
# Вывод заданных объектов на экран
    print(f"{human_readable_size(size):}\t{item}")

# Для выполнения только при явном запуске файла
if __name__ == "__main__":
  main()

