choice = 0
while (choice != 5):
    num1 = int(input("Enter the value of number 1: "))
    num2 = int(input("Enter the value of number 2: "))
    
    print("Enter 1 for Addition")
    print("Enter 2 for Substraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division")
    print("Enter 5 for Terminate")
    
    choice = int(input("Enter your choice : "))


    match choice:

        case 1:
            print("This is the answer of your Addition ", num1 + num2)

        case 2:
            print("This is the answer of your Substraction ", num1 - num2)

        case 3:
            print("This is the answer of your Multiplication ", num1 * num2)

        case 4:
            print("This is the answer of your Division ", num1 / num2)
        
        case 5:
            print("Thank You !")

        case _:
            print("Entered an invalid choice !!!")
        