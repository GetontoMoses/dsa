# to do list
def show_tasks(tasks):
    if not tasks:
        print("Sorry there are no tasks")
        
    else:
        print("Here are your tasks")
        for i, items in enumerate(tasks,1): # the function iterates over the the list to get both index and the value of an item
            print(f"{i}.{items}")


def main():
    tasks = []

    print(" options:\n add task = 1\n view tasks = 2\n delete task = 3")
    option = int(input("Please select an option:\n"))

    # add a task
    if option == 1:
        name = input("Enter the Task:\n")
        tasks.append(name)
    if option == 2:
        name = input("Here are the Tasks in the list:\n")
        show_tasks()
    if option == 3:
        name = int(input("Enter the Task to be removed:\n"))
        tasks.remove(name)
       
            
    else:
        print("Invalid input: Please choose one option")

main()
