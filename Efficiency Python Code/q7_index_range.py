  
""" Question 7: index_range """
"""
Inputs: list L and integer target
Output: indexes where target first and last appears in L
"""
def binary_search(L,target):
    st=0
    end=len(L)-1
    while(st<=end):
        mid=(st+end)//2
        if L[mid]==target:
            return True
        elif L[mid]>=target:
            end=mid-1
        else :
            st=mid+1
def find_low_index(L,target):
    st=0
    end=len(L)-1
    while(st<=end):
        mid=(st+end)//2
        if L[mid]>=target:
            end=mid-1
        else :
            st=mid+1
    return st
def find_high_index(L,target):
    st=0
    end=len(L)-1
    while(st<=end):
        mid=(st+end)//2
        if L[mid]>target:
            end=mid-1
        else:
            st=mid+1
    return st-1

def index_range(L, target):
    if not (binary_search(L,target)):
        return [-1,-1]
    low=find_low_index(L,target)
    high=find_high_index(L,target)
    return [low,high]

    # return
# print(index_range([1,1,2,2,3],3))
""" Test 7"""  
def test_index_range():
    print("Testing index_range...", end="")
    assert(index_range([1, 1, 2, 3, 3, 3], 1) == [0, 1])
    assert(index_range([1, 1, 2, 3, 3, 3], 2) == [2, 2])
    assert(index_range([1, 1, 2, 3, 3, 3], 3) == [3, 5])
    assert(index_range([1, 1, 2, 3, 3, 3], 4) == [-1, -1])
    print("Passed!")


if __name__ == '__main__':
    test_index_range()