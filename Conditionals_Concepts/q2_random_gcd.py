""" Question 2: random_gcd() """
"""
Inputs: None
Output: randomly generates two integers in range [1, 100] and returns gcd
"""
import random
import math
def random_gcd():
    value_1=(random.randint(1,100))
    Value_2=(random.randint(1,100))
    print(value_1,Value_2)
    GCD=(math.gcd(value_1,Value_2))
    print ("X Y", str(value_1)+" "+str( Value_2) ,sep=":")
    return GCD


""" Test 2 """
def test_random_gcd():
    print("Testing random_gcd...")
    # Check whether the result is actually the GCD of the two printed numbers
    result = random_gcd() # should print x and y
    print("gcd:", result) # prints the result
    print("... done!")

if __name__ == '__main__':
    test_random_gcd()