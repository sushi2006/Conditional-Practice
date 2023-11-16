days =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
def day_of_week(day): 
  return days[day % 7]
today = int(input("Enter today's day of the week as an integer (1 for Monday, 2 for Tuesday, ..., 0 for Sunday): ")) 
days_after = int(input("Enter the number of days after today for a future day: "))
future_day = today + days_after 
print("The future day of the week is:", day_of_week(future_day))