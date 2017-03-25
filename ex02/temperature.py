####################################
# temperature.py
#
# Introduce mathematical operations
# Introduce formatted printing
####################################

from cs50 import get_float

print("What temperature is it in Fahrenheit?")
fahrenheit = get_float()

# formula for conversion is (f - 32) * (5/9)

celsius = 5.0 / 9.0 * (fahrenheit - 32.0)

# print my floating point number (f) to one decimal place (1)
print("{:.1f}".format(celsius))
