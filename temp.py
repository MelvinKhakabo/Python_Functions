#function that converts a temperature from Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return(celsius * 9/5)+ 32
temp_celsius = 25
temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C is {temp_fahrenheit}°F")