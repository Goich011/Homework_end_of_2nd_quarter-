from Note import *
import csv

def importNote(): #Ипортировать заметку
    notes = []
    with open('Python/Notes.csv', 'r') as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            note = Note(row[0], row[1], row[2], row[3])
            notes.append(note)
    print("Ипортированно")
    return notes


def exportNote(notes): # Экспортировать заметку
    if (len(notes) > 0):
        with open('Python/Notes.csv', 'w') as f:
            writer = csv.writer(f, delimiter=";", lineterminator="\r")
            for x in notes:
                writer.writerow([x.title, x.body, x.date, x.id])
        print("Заметка сохранена!")
    else:
        print("Заметки отсутствуют!")
