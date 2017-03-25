####################################
# conditions.py
#
# Introduce decision making
####################################

import cs50

print("Give me an integer, please!")
i = cs50.get_int()

# if the condition is true, execute the indented lines of code
if i < 0:
    print("negative")

# "elif" is the way one says "else if"
elif i > 0:
    print("positive")
    
# else is the catch-all
else:
    print("zero")
