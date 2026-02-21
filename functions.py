def read_todo(filename="todos.txt"):
    with open(filename, "r") as file1:
        todos1 = file1.readlines()
        return todos1

def write_todo(todos,filename="todos.txt"):
    with open(filename, "w") as file1:
        file1.writelines(todos)

if __name__ =="__main__":
    print("Good Bye!!")
    print(read_todo())