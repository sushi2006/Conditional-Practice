# Function to convert a percentage to a letter grade
def convert_percentage_to_letter_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

# Ask the user for their test percentage
test_percentage = int(input("Enter your test percentage: "))

# Convert the percentage to a letter grade
letter_grade = convert_percentage_to_letter_grade(test_percentage)

# Output the letter grade and the percentage
print(f"A {test_percentage} you have earned a {letter_grade}")