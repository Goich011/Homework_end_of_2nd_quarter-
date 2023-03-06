from Note import *
from ImportExport import *
import datetime

def main(): # запуск приложения
    notes = []
    done = False
    while(done == False):
        print("Приложение Заметки \n\
              1 - Создать заметку \n\
              2 - Редактировать заметку \n\
              3 - Показать все заметки \n\
              4 - Вставить заметку из файла \n\
              5 - Отправить заметку в файл \n\
              6 - Удалить заметку \n\
              0 - Выход из приложения")
        command = input("Какое действие выполнить? ")
        match command:
            case "1":
                notes.append(addNote(notes))
                print("Заметка создана")
            case "2":
                editNote(notes)
            case "3":
                showAllNotes(notes)
            case "4":
                importNote(notes)
            case "5":
                exportNote(notes)
            case "6":
                deleteNote(notes)
            case "0":
                print("Выключение")
                done = True
            case _:
                print("Не корректная команда")

def inputData(notes): #Запись заметки
    dimens = len(notes)
    name = input("Название заметки: ")
    content = input("Заметка: ")
    now = datetime.datetime.now()
    return [name, content, now.strftime("%d-%m-%Y %H:%M"), dimens]  

def addNote(notes): #Добавление заметки
    noteinfo = inputData(notes)
    return Note(noteinfo[0], noteinfo[1], noteinfo[2], noteinfo[3])

def editNote(notes): #Редактироваине
    if (len(notes) > 0):
        index = input("Какую заметку требуется отредактировать? введите ID: ")
        try:
            i = int(index)
            if (i < len(notes)):
                notes[i] = addNote(notes)
                print("Отредактированно!")
            else:
                print(
                    "Некорректный ввод")
        except ValueError:
            print("Некорректный ввод!")
    else:
        print("Заметка пустая")

def deleteNote(notes): #Удаление
    if (len(notes) > 0):
        index = input("Какую заметку требуется удалить? введите ID")
        try:
            i = int(index)
            if (i < len(notes)):
                notes.pop[i]
                print("Удалено!")
            else:
                print(
                    "Некорректный ввод")
        except ValueError:
            print("Некорректный ввод!")
    else:
        print("Заметка пустая")

def showAllNotes(data): 
    if len(data) > 0:
        for object in data:
            print(object.printNote())
    else:
        print("Заметки отсутствуют")