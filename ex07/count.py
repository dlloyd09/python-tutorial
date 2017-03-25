####################################
# count.py
#
# Introduce range() for counting
####################################

import cs50

print("Please give me an integer!")
value = cs50.get_int()

for i in range(value):
    print(i + 1)