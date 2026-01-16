print("~~~~~~~~~🧑‍💻🧑‍💻welcome the to do list🧑‍💻🧑‍💻~~~~~~~~~~ ")
 
task=[]

while True:
    print("Enter the cohies :\n")
    print("1. add task ")   # مشان نضيف على القائمه
    print("2. viwe task")   #مشان نعرض القائمه     
    print("3. delet task")  # مشان نحذف الي بدنا اياه من القائمه
    print("4. Exit")        # مشان نخرج  من البرنامج
    print("-|-|-|-|-|-|-|-|-|-|-|-|-|-|-")

    cohies=input("enter your (1 - 4) : ")

    if cohies=="1":
        value=input(" Your add the input new: ")
        task.append(value)
        print("✅true add✅:")
    elif cohies=="2":
        if not task:
            print("❌ dont add task ❌")
        else:
            print("Your task :")
            i=1
            for data in task:
                print(i,data)
                i+=1
    elif cohies=="3":
        if not task:
            print("❌ dont add task ❌")
        else:
            print("Your task :")
            i=1
            for data in task:
                print(i,data)
                i+=1

        dd=input("enter the number task to delete👉:")
        dd=int(dd)
        task.pop(dd)
        print(task)
    elif cohies=="4":
        print("thank you for ues progrem")
        break # مشان نوقف استخدام البرنامج 
    else:
        print("🤷‍🤷‍eror the cohies 🤷‍🤷‍")
        break

            

