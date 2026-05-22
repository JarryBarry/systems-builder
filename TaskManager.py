class Task:
    def __init__(self, title):
        self.title = title
        self.is_done = False

    def mark_done(self):
        self.is_done = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)

    def show_tasks(self):
        i = 0
        for t in self.tasks:
            print(f"{i}.{t.title} {t.is_done} ")
            i += 1

    def get_stats(self):
        stats = {
            "completed" : 0,
            "pending" : 0,
            "length" : len(self.tasks)
        }
        for i in self.tasks:
            if i.is_done == True:
                stats["completed"] += 1
            else:
                stats["pending"] += 1
        return stats
        

manager = TaskManager()
while True:
    action = input("What would you like to do? (add/show/finish/stats/quit) \n")
    if action.lower() == "add":
        title = input("Enter your task\n")
        manager.add_task(title)
    elif action.lower() == "show":
        manager.show_tasks()
    elif action.lower() == "finish":
        manager.show_tasks()
        number = input("Choose the task number\n") #I will assume the user inputs only numbers due to this being practice
        manager.tasks[int(number)].mark_done()
    elif action.lower() == "stats":
        stats = manager.get_stats()
        print (stats)
    elif action.lower() == "quit":
        break
    else:
        print("Please input a valid option")