""" Question 12: longest_bit_run """
"""
Input: string s of 0s and 1s
Output: the length of the longest run of 0s or 1s
"""


def longest_bit_run(s):
    previous=-1
    current=0
    max_count=0
    for bit in s:
        if (bit==previous):
            current+=1
        else:
            current=1
        if(current>max_count):
                max_count=current
        previous=bit 
    return  max_count

""" Test 12 """
def test_longest_bit_run():
    print("Testing longest_bit_run...", end='')
    assert(longest_bit_run('0') == 1)
    assert(longest_bit_run('011') == 2)
    assert(longest_bit_run('0000') == 4)
    assert(longest_bit_run('01') == 1)
    assert(longest_bit_run('00111100') == 4)
    print("... done!")


if __name__ == '__main__':
    test_longest_bit_run()