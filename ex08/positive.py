####################################
# positive.py
#
# Introduce the concept of functions
# Introduce the concept of main
# Bring it all together?
####################################

import cs50

def get_positive_int():
    # continue looping forever
    while True:
        
        # prompt the user for input using CS50's get_int function
        print("n is ", end="")
        n = cs50.get_int()
        
        # if we get a positive integer, break out of the loop
        if n > 0:
            break
    
    # return  a value from this function back to the user    
    return n

def main():
    
    i = get_positive_int()
    print("{} is a positive integer".format(i))



if __name__ == "__main__":
    main()
