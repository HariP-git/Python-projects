class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "[x]" if self.done else "[ ]"
        return f"{status} {self.title}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f"Added task: '{title}'")

    def update_task(self, index, new_title):
        if 0 <= index < len(self.tasks):
            self.tasks[index].title = new_title
            print(f"Updated task {index + 1} to '{new_title}'")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Deleted task: '{removed_task.title}'")
        else:
            print("Invalid task number.")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            print(f"Marked task {index + 1} as done.")
        else:
            print("*******Invalid task number.*********")

    def show_tasks(self):
        if not self.tasks:
            print("-----------No tasks in the list.---------")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")


def main():
    todo_list = ToDoList()

    while True:
        print("\n**********To-Do List Menu: ************")
        print("1. Add task")
        print("2. Update task")
        print("3. Delete task")
        print("4. Mark task as done")
        print("5. Show tasks")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            title = input("Enter the task title: ")
            todo_list.add_task(title)

        elif choice == '2':
            todo_list.show_tasks()
            index = int(input("Enter task number to update: ")) - 1
            new_title = input("Enter new task title: ")
            todo_list.update_task(index, new_title)

        elif choice == '3':
            todo_list.show_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)

        elif choice == '4':
            todo_list.show_tasks()
            index = int(input("Enter task number to mark as done: ")) - 1
            todo_list.mark_done(index)

        elif choice == '5':
            todo_list.show_tasks()

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
