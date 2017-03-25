####################################
# logical.py
#
# Introduce Boolean concepts (or, and)
####################################

import cs50

print("Answer yes (y/Y) or no (n/N)")
c = cs50.get_char()

if c == "Y" or c == "y":
    print("yes")
elif c == "N" or c == "n":
    print("no")
else:
    print("error")
