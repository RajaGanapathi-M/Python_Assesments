""" Question 8: is_lower """
"""
Input: string s
Output: True if s contains at least one character and every char is lowercase
        False otherwise
"""
def is_lower(s):
    if s=="":return False
    for c in s:
        if ("a"<= c <= "z")or("0"<=c <="9"):
            return True
        if ("A"<=c <="Z"):return False
    return True

""" Test 8 """
def test_is_lower():
    print("Testing is_lower...", end='')
    assert(is_lower("") == False)
    assert(is_lower("a") == True)
    assert(is_lower("123a") == True)
    assert(is_lower("Hello") == False)
    assert(is_lower("hello!") == True)
    print("... done!")

if __name__ == '__main__':
    test_is_lower()