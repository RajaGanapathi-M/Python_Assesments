
""" Question 7: generate_coin_sequences """
"""
Input: integer n
Output: 2D list containing all combinations of n "H"s and "T"s
"""
def generate_coin_sequences(n):
    if n==0:
        return[[]]
    else:
        result=[]
        value=generate_coin_sequences(n-1)
        for lst in (value):
            result.append(lst+["H"])
            result.append(lst+["T"])
    return result

""" Test 7 """
def test_generate_coin_sequences():
    print("Testing generate_inputs...", end="")
    assert(sorted(generate_coin_sequences(3)) == [ ["H","H","H"], ["H","H","T"], ["H","T","H"], ["H","T","T"],
                                           ["T","H","H"], ["T","H","T"], ["T","T","H"], ["T","T","T"] ])
    assert(sorted(generate_coin_sequences(1)) == [ ["H"], ["T"] ])
    assert(sorted(generate_coin_sequences(5)) == [ ["H","H","H","H","H"], ["H","H","H","H","T"], ["H","H","H","T","H"], ["H","H","H","T","T"],
                                           ["H","H","T","H","H"], ["H","H","T","H","T"], ["H","H","T","T","H"], ["H","H","T","T","T"],
                                           ["H","T","H","H","H"], ["H","T","H","H","T"], ["H","T","H","T","H"], ["H","T","H","T","T"],
                                           ["H","T","T","H","H"], ["H","T","T","H","T"], ["H","T","T","T","H"], ["H","T","T","T","T"],
                                           ["T","H","H","H","H"], ["T","H","H","H","T"], ["T","H","H","T","H"], ["T","H","H","T","T"],
                                           ["T","H","T","H","H"], ["T","H","T","H","T"], ["T","H","T","T","H"], ["T","H","T","T","T"],
                                           ["T","T","H","H","H"], ["T","T","H","H","T"], ["T","T","H","T","H"], ["T","T","H","T","T"],
                                           ["T","T","T","H","H"], ["T","T","T","H","T"], ["T","T","T","T","H"], ["T","T","T","T","T"] ])
    print("... done!")



if __name__ == '__main__':
    test_generate_coin_sequences()
