""" Question 4: recursive_greater_count """
"""
Input: two lists
Output: count of indices where the values in list1 is greater than list2
"""
def recursive_greater_count(lst1, lst2):
    if (len(lst1)==0) or (len(lst2)==0):
        return 0
    else:
        left_1=lst1[0]
        left_2=lst2[0]
        partial_re=recursive_greater_count(lst1[1:],lst2[1:])
        if (left_1)>(left_2):
           return 1+ partial_re

    return partial_re

""" Test 4 """
def test_recursive_greater_count():
    print("Testing recursive_greater_count...", end='')

    assert(recursive_greater_count([5, 2, 9, 1], [3, 4, 7, 1]) == 2)
    assert(recursive_greater_count([1, 2, 3], [3, 2, 1]) == 1)
    assert(recursive_greater_count([10, 20], [5, 15]) == 2)
    assert(recursive_greater_count([], [1, 2, 3]) == 0)

    print("... done!")

if __name__ == '__main__':
    test_recursive_greater_count()
