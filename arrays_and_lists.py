# to do list
def show_tasks(tasks):
    if not tasks:
        print("Sorry there are no tasks\n")
        
    else:
        print("Here are your tasks")
        for i, items in enumerate(tasks,1): # the function iterates over the the list to get both index and the value of an item
            print(f"{i}.{items}")


def main():
    tasks = []
    while True:
        print(" options:\n add task = 1\n view tasks = 2\n delete task = 3\n Exit = 4")
        option = int(input("Please select an option:\n"))
    
        # add a task
        if option == 1:
            name = input("Enter the Task:\n")
            tasks.append(name)
            
            print(f"Task : {name} added.")
            
        #Search
        elif option == 2:
            show_tasks(tasks)
            
        #Remove tasks
        elif option == 3:
            show_tasks(tasks)
            name = int(input("Enter the Task to be removed:\n"))
            if 1<= name <=len(tasks):
                removed = tasks.pop(name - 1)
                print(f"{removed} : removed")
        
        elif option == 4:
            print("Exiting TO - Do manager") 
            break  
                
        else:
            print("Invalid input: Try again")

main()
