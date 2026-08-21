""" Question 2: count_sums_with_end_digit """
"""
Input: two integers
Output: all sums of n between 1+n and n+n that end in specified digit
"""
def count_sums_with_end_digit(n, digit):
    count=0
    for i in range (1,n+1):
        for j in range (1,n+1):
            add=i+j
            if add%10==digit:
                count+=1
    return count

""" Test 2 """
def test_count_sums_with_end_digit():
    print("Testing count_sums_with_end_digit...", end='')
    
    assert(count_sums_with_end_digit(3, 2) == 1)
    assert(count_sums_with_end_digit(4, 5) == 4)
    assert(count_sums_with_end_digit(5, 0) == 1)
    assert(count_sums_with_end_digit(2, 3) == 2)
    
    print("... done!")


if __name__ == '__main__':
    test_count_sums_with_end_digit()