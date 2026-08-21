""" Question 1: get_digit_string """
"""
Input: 2D list
Output: string of all the digits in the list, reading left to right, top to bottom
"""
def get_digit_string(lst):
    result=""
    for row in lst:
        for c in row:
            if ("0"<=c<="9"):
                result+=c
    return result

""" Test 1 """
def test_get_digit_string():
    print("Testing get_digit_string...", end='')
    
    assert(get_digit_string([
        ['a', '1', 'b'],
        ['2', 'x', '3'],
        ['y', 'z', '4']
    ]) == "1234")

    assert(get_digit_string([
        ['0', 'a'],
        ['b', '9']
    ]) == "09")

    assert(get_digit_string([
        ['x', 'y'],
        ['z', 'a']
    ]) == "")

    print("... done!")


if __name__ == '__main__':
    test_get_digit_string()