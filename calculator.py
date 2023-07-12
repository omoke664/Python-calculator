#HERE IS A CALCULATOR APP CREATED USING PYTHON
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def remainder(x,y):
    return x % y

print("Welcome to the python calculator app")

while True:
    print("Please select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Remainder")
    print("6. Exit")
    choice= input("Enter your choice of operation:")
    
    if choice == '6':
        print("Exiting the calculator App. Goodbye!")
        break
    
    num1 = int(input("Enter your first number:"))
    num2 = int(input("Enter the second number:"))
    
    if choice == '1':
        result = add(num1,num2)
    elif choice =='2':
        result = subtract(num1,num2)
    elif choice =='3':
        result = multiply(num1,num2)
    elif choice =='4':
        result = divide(num1,num2)
    elif choice =='5':
        result = remainder(num1,num2)
    else:
        print("Invalid choice, select another option!!")
        continue
    print("Result:",result)
    

    
    
    