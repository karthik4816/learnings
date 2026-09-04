import json

with open("tasks.json", "r") as file:
    tasks = json.load(file)

print("1.add task")
print("2.view task")
print("3.remove task")
print("4.exit")
while True:
    choice =int(input("enter your choice: "))
    if choice == 1:
         task = input("enter your task: ")
         tasks.append(task)
         print("task added")
        
         with open("tasks.json", "w") as file:
             json.dump(tasks, file, indent=4)
        
    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks found")
        else:
             print("your tasks: ")
             for i in range(len(tasks)):
                print(i + 1, tasks[i])
    elif choice == 3:
        if len(tasks) == 0:
           print("No tasks found")
        else:
            task = int(input("enter the number to remove: "))
            tasks.pop(task - 1)
            print("task removed")
           
            with open("tasks.json", "w") as file:
                 json.dump(tasks, file, indent=4)
    
    elif choice == 4:
         print("Goodbye!")
         break        