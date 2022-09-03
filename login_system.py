import random

members = []
members_ID = []

while True:
    
    choice_1 = input("Do you have an account ? [YES/NO]\n").upper()
    if choice_1 == "NO":
        print("Complete your information below.")
        
        while True:
            user_id = input ("Enter your user ID: ").lower()
            if user_id not in members_ID:
                members_ID.append(user_id)
                break
            else:
                print("This user ID already exits. Please enter another ID. ")
                continue
            
        while True:
            user_password = input("Enter your password :")
            repeat_password =  input("Repeat your password :")
            if repeat_password ==  user_password:
                break
            else:
                print("Password does not match, try again")
                continue
        
        while True:
            num1 = random.randint(10,40)
            num2 = random.randint(10,40)
            print(f"Enter the correct number {num1} + {num2} = ?")
            num3 = int(input())
            if num3 == num1 + num2:
                print("Rigisterion completed !\n")
                user_identity = user_id + user_password
                members.append(user_identity)
                break
            else:
                print("The number you entered wasn't correct!")
                continue
        continue
    elif choice_1 == "YES":
        user_id = input("Enter your ID : ")
        user_password = input("Enter your password : ")
        user_identity = user_id + user_password
        if user_identity in members:
            print("Wel come back dear @ ", user_id)
            input()
            break
        if user_identity not in members:
            print("Given information you entered wrong !")
            continue
    else:
        print("<<< You must choose between YES and NO >>>")
        continue