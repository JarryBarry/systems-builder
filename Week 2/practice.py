#lists
movies = ["Shrek", "Cars", "Toys Story"]
movies.append("Harry Potter")
for movie in movies:
    print(movie)

#dictionary
task1 = {
    "title" : "Buy Groceries",
    "priority" : "Low",
    "is_done" : False
}

print (task1)

task1["is_done"] = True
print (task1["title"])

#OOP
class Task:
    def __init__(self, title):
        self.title = title
        self.is_done = False
    def mark_done(self):
        self.is_done = True


task1 = Task("Buy Groceries")
print(task1.title + " " + str(task1.is_done))
task1.mark_done()
print (f"{task1.title} {task1.is_done}")
