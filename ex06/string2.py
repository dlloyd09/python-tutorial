####################################
# string2.py
#
# Introduce a new kind of loop
# Introduce the concept of "None"/null
####################################

import cs50

print("Please provide some text!")
s = cs50.get_string()

if s != None:
    for c in s:
        print(c)
