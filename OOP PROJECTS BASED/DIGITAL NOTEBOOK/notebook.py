import os
import base64
from datetime import datetime

class Note:
    def __init__(self, title, content, timestamp=None):
        self.title = title
        self.content = content
        self.timestamp = timestamp or datetime.now().isoformat()

    def view(self):
        print(f"\nTitle: {self.title}\nContent: {self.content}\nCreated on: {self.timestamp}")

    def edit(self, new_content):
        self.content = new_content
        self.timestamp = datetime.now().isoformat()

    def to_string(self, category_name):
        return f"Category: {category_name}\nTitle: {self.title}\nContent: {self.content}\nTimestamp: {self.timestamp}\n---\n"

    @classmethod
    def from_string(cls, lines):
        title = lines[1].split(": ", 1)[1].strip()
        content = lines[2].split(": ", 1)[1].strip()
        timestamp = lines[3].split(": ", 1)[1].strip()
        return cls(title, content, timestamp)


class Category:
    def __init__(self, name):
        self.name = name
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)
        print(f"\n✅ Note '{note.title}' added to category '{self.name}'.")

    def remove_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                print(f"\n🗑️ Note '{title}' removed.")
                return
        print("\n⚠️ Note not found.")

    def list_notes(self):
        if not self.notes:
            print("\n📭 No notes available.")
        for note in self.notes:
            print("-" * 40)
            note.view()

    def save_to_file(self, filename):
        with open(filename, "ab") as file:
            for note in self.notes:
                encoded = base64.b64encode(note.to_string(self.name).encode("utf-8"))
                file.write(encoded + b"\n")
        print(f"\n💾 Encrypted notes saved to '{filename}'.")

    def load_from_file(self, filename):
        try:
            with open(filename, "rb") as file:
                lines = file.readlines()

            self.notes = []
            for encoded in lines:
                try:
                    decoded = base64.b64decode(encoded).decode("utf-8")
                    block = decoded.strip().split("\n")
                    if block and block[0].strip().endswith(self.name):
                        note = Note.from_string(block)
                        self.notes.append(note)
                except Exception:
                    continue
            print(f"\n📥 Loaded notes for category '{self.name}'.")
        except FileNotFoundError:
            print(f"\n❌ File '{filename}' not found.")


def list_saved_files():
    print("\n📂 Saved .txt Files:")
    files = [f for f in os.listdir() if f.endswith(".txt")]
    if not files:
        print("(No files found)")
    else:
        for file in files:
            print(f"- {file}")


def menu():
    current_category = None

    while True:
        print("""
📒 DIGITAL NOTEBOOK MENU
1. Create New Category
2. Add Note
3. View Notes
4. Edit Note
5. Delete Note
6. Save Notes to File
7. Load Notes from File
8. Show Saved Files
9. Exit
        """)

        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            name = input("Enter category name: ").strip()
            current_category = Category(name)
            print(f"\n📁 Category '{name}' created.")

        elif choice == "2":
            if current_category:
                title = input("Enter note title: ").strip()
                content = input("Enter note content: ").strip()
                current_category.add_note(Note(title, content))
            else:
                print("\n⚠️ Create a category first.")

        elif choice == "3":
            if current_category:
                current_category.list_notes()
            else:
                print("\n⚠️ No category selected.")

        elif choice == "4":
            if current_category:
                title = input("Enter title of note to edit: ").strip()
                for note in current_category.notes:
                    if note.title == title:
                        new_content = input("Enter new content: ")
                        note.edit(new_content)
                        print("\n✏️ Note updated.")
                        break
                else:
                    print("\n⚠️ Note not found.")
            else:
                print("\n⚠️ No category loaded.")

        elif choice == "5":
            if current_category:
                title = input("Enter note title to delete: ").strip()
                current_category.remove_note(title)
            else:
                print("\n⚠️ Load a category first.")

        elif choice == "6":
            if current_category:
                file = input("Enter filename to save to (e.g., notes.txt): ").strip()
                current_category.save_to_file(file)
            else:
                print("\n⚠️ No category to save.")

        elif choice == "7":
            name = input("Enter category name to load: ").strip()
            file = input("Enter filename to load from: ").strip()
            current_category = Category(name)
            current_category.load_from_file(file)

        elif choice == "8":
            list_saved_files()

        elif choice == "9":
            print("\n👋 Exiting Notebook. Goodbye!")
            break

        else:
            print("\n❌ Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
