""" Question 6: recursive_expand_pairs """
"""
Input: string s
Output: string with each character duplicated

"""
def recursive_expand_pairs(s):
    if s=="":
        return ""
    else:
        left=s[0]
        partial=recursive_expand_pairs(s[1:])
        return left+left+partial


""" Test 6 """
def test_recursive_expand_pairs():
    print("Testing recursive_expand_pairs...", end='')

    assert(recursive_expand_pairs("abc") == "aabbcc")
    assert(recursive_expand_pairs("hello") == "hheelllloo")
    assert(recursive_expand_pairs("x") == "xx")
    assert(recursive_expand_pairs("") == "")

    print("... done!")

if __name__ == '__main__':
    test_recursive_expand_pairs()
