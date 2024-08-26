#function that takes three numbers as arguments and returns the maximum of the three
def find_max(num1, num2, num3):
    return max (num1, num2, num3)

result = find_max(10, 20, 15)
print("The maximum value is:", result)


#find minimum
def find_min(num1, num2, num3):
    return min (num1, num2, num3)
result = find_min(10, 30, 20)
print("The minimum value is:", result)


#sum
def add_numbers(num1, num2, num3):
    result = num1 + num2 + num3
    return result
number_1 = 20
number_2 = 30
number_3 = 40
result = add_numbers(number_1, number_2, number_3)
print("The sum is:", result)