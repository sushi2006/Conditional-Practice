# Ask user to enter a three-digit integer
num = input("Enter a three-digit integer: ")

# Check if the number is a three-digit integer
if len(num) != 3 or not num.isdigit():
    print("Invalid input. Please enter a three-digit integer.")
else:
    # Check if the number is a palindrome
    if num == num[::-1]:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")