num1 = int(input("Enter the first integer: ")) 
num2 = int(input("Enter the second integer: ")) 
num3 = int(input("Enter the third integer: "))

def non_decreasing_order(num1, num2, num3): 
  #ordered incase number 1 is the smallest
  if num1 <= num2 <= num3: 
    return (num1, num2, num3)
  #ordered incase number 1 is the smallest but the second number is not
  elif num1 <= num3 <= num2: 
    return (num1, num3, num2) 
    #ordered incase number 2 is the smallest
  elif num2 <= num1 <= num3: 
    return (num2, num1, num3) 
    #ordered incase number 2 is the smallest but the first number is not
  elif num2 <= num3 <= num1: 
    return (num2, num3, num1) 
  #ordered incase number 3 is the smallest
  elif num3 <= num1 <= num2: 
    return (num3, num1, num2) 
  #ordered in the last possible way
  else: 
    return (num3, num2, num1)

print("the numbers in non-decreasing order are:",non_decreasing_order(num1, num2, num3))