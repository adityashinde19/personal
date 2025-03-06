from app.basic_operations import add, subtract, multiply, divide
from app.advanced_operations import power, square_root, logarithm, factorial
from app.trigonometry import sine, cosine, tangent

def main():
    print("Welcome to the Scientific Calculator")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    print("5. Power\n6. Square Root\n7. Logarithm\n8. Factorial")
    print("9. Sine\n10. Cosine\n11. Tangent")

    choice = int(input("Enter your choice (1-11): "))

    if choice in [1, 2, 3, 4, 5]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        elif choice == 4:
            print("Result:", divide(num1, num2))
        elif choice == 5:
            print("Result:", power(num1, num2))

    elif choice in [6, 7, 8]:
        num = float(input("Enter the number: "))
        if choice == 6:
            print("Result:", square_root(num))
        elif choice == 7:
            base = float(input("Enter base (default is 10): ") or 10)
            print("Result:", logarithm(num, base))
        elif choice == 8:
            print("Result:", factorial(int(num)))

    elif choice in [9, 10, 11]:
        angle = float(input("Enter the angle in degrees: "))
        if choice == 9:
            print("Result:", sine(angle))
        elif choice == 10:
            print("Result:", cosine(angle))
        elif choice == 11:
            print("Result:", tangent(angle))

    else:
        print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
