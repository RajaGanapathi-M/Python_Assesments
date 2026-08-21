
""" Question 5: recursive_count_digits """
"""
Input: integer n
Output: count of digits in n
        must be solved recursively
"""
def recursive_count_digits(n):
    n=abs(n)
    if n<=9:
        return 1
    else:
      return 1+  recursive_count_digits(n//10)

""" Test 5 """
def test_recursive_count_digits():
    print("Testing recursive_count_digits...", end='')

    assert(recursive_count_digits(1234) == 4)
    assert(recursive_count_digits(0) == 1)
    assert(recursive_count_digits(-567) == 3)
    assert(recursive_count_digits(9) == 1)

    print("... done!")

if __name__ == '__main__':
    test_recursive_count_digits()
