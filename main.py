user_name = input("Username : ")
print(f"Welcome {user_name} to TO DO LIST PROGRAM !!! ")
print("-----------------------------------------------")
print("---------------- LETS START -------------------")

info = []

while True:
    print("View List Press 1")
    print("Add List Press 2")
    print("Delete List Press 3")
    print("Exit Press 4")

    choice = int(input("Which Option do you like ? : "))
    print("-------------------------------------------")

    if choice == 1:
        if len(info) == 0:
            print("NO DESCRIPTION IN LIST !!!")
            print("==========================")
        else:
            for i, task in enumerate(info, start=1):
                print(i, task)
            print("==========================")
                
    elif choice == 2 :
        info_add = input("Description : ")
        info.append(info_add)
        print(f"ADD DESCRIPTION : {info_add} COMPLETE !!!")
        print("==========================")
    elif choice == 3 :
        if len(info) == 0 :
            print("NO DESCRIPTION IN LIST")
        else :
            for i , task in enumerate(info,start = 1) :
                print(f"{i}. Detail : {task}")
            delete_num = int(input(f"Which number {user_name} want to delete ? : "))
            if 1 <= delete_num <= len(info) :
                remove = info.pop(delete_num -1 )
                print("==========================")
            else :
                print("Error Invalid number")
    elif choice == 4 :
        print("Goodbye !!!")
        break 
    else :
        print("Error Valid command !! ")
        