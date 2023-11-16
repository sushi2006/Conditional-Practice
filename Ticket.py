import random

def ticket_result(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2

# Assume these values for the user's speed and whether it is their birthday
user_speed = 85
is_birthday = False

# Calculate the result
result = ticket_result(user_speed, is_birthday)

# Print the result
print(f"The result is: {result}")