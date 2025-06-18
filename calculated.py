def factorial(n):
    """Calculate factorial of a non-negative integer n recursively."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Please enter a non-negative integer.")
                continue
            result = factorial(num)
            print(f"The factorial of {num} is {result}.")
            break
        except ValueError:
            print("That's not a valid integer. Please try again.")

if __name__ == "__main__":
    main()
