""" Question 7: get_grade """
"""
Inputs: five integers representing grades and an optional integer for the curve
        (curve defaults to 0 if no curve specified)
Output: prints average grade before curve is applied
        returns average grade after curve applied
"""
# Create the function header yourself!

def get_grade(a,b,c,d,e,curve=0):
    val_tot=(a+b+c+d+e)
    mini=min(a,b,c,d,e)
    avg=val_tot - mini
    Tot_avg=avg/4
    nvn=Tot_avg+ (curve)
    print("Pre curve : "+str(Tot_avg))
    return nvn

""" Test 7 """
def test_get_grade():
    print("Testing get_grade...")
    assert(get_grade(82, 93, 87, 64, 91) == 88.25) # prints "Average grade pre-curve: 88.25"
    assert(get_grade(75, 80, 85, 90, 95, curve=2) == 89.5) # prints "Average grade pre-curve: 87.5"
    assert(get_grade(75, 75, 75, 75, 75, curve=10) == 85) # prints "Average grade pre-curve: 75.0"
    print("... done!")

if __name__ == '__main__':
    test_get_grade()