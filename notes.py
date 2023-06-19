
import json
import datetime
from tkinter.filedialog import askopenfilename, asksaveasfilename
import io

notes = []

def create_note():
    global notes
    note_id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    try:
        body = input("Введите текст заметки: ").strip()
    except Exception as e:
        print("Произошла ошибка ввода: ", e)
        body = ""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": note_id, "title": title, "body": body, "timestamp": timestamp}
    notes.append(note)
    save_file()
    print("Заметка создана.")

def read_notes():
    print("Список заметок:")
    for note in notes:
        print(f"{note['id']}. {note['title']} ({note['timestamp']})")

def edit_note():
    global notes
    note_id = int(input("Введите id заметки: "))
    for note in notes:
        if note["id"] == note_id:
            note["title"] = input("Введите новый заголовок для заметки: ")
            try:
                note["body"] = input("Введите новый текст для заметки: ").strip()
            except Exception as e:
                print("Произошла ошибка ввода: ", e)
                note["body"] = ""
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_file()
            print("Заметка успешно изменена.")
            return
    print("Заметка с таким id не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки, которую необходимо удалить: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_file()
            print("Заметка удалена.")
            return
    print("Заметка с таким ID не найдена.")

def save_file():
    file_name = asksaveasfilename(defaultextension=".json")
    if file_name:
        with io.open(file_name, "w", encoding="utf-8") as f:
            json.dump(notes, f, ensure_ascii=False)

def load_file():
    try:
        file_name = askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_name:
            with io.open(file_name, "r", encoding="utf-8") as f:
                global notes
                notes = json.load(f)
    # except Exception as e:
    #     print("Ошибка загрузки файла:", e)
    except:
        pass

def main():
    load_file()
    while True:
        print("\n1. Создать заметку\n2. Список заметок\n3. Редактировать заметку\n4. Удалить заметку\n5. Сохранить заметки и выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            save_file()
            break
        else:
            print("Выберите правильное действие.")

if __name__ == "__main__":
    main()
    