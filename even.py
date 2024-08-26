#this function checks if a number is even or odd
def is_even(number):
  return number % 2 == 0
num = 8
if is_even(num):
  print(f"{num} is even. ")
else:
  print(f"{num} is odd. ")