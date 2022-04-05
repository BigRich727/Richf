while True:
    try:
        first_number = int(input("What is the first number you want to add?"))
        second_number = int(input("What is the second number you want to add"))
        sum = first_number + second_number
        print('the sum of the two numbers is',sum)       
    except: 
        print("You are so silly. That is not an integer...")

