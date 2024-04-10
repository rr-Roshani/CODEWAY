print("Welcome To Simple Calculator")
def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Available Choices:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Enter Your Choice 1-4: "))
    if choice == 1:
        print("The sum of Two Number is ",num1+num2)
    elif choice == 2:
        print("The Difference of Two Number is ",num1-num2)
    elif choice == 3:
        print("The Product of Two Number is",num1*num2)
    elif choice == 4:
        print("The Division Of Two Number is",num1/num2)
    else:
        print("Invalid Input")
    main()

main()
