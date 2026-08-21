
""" Question 3: process_student_grades """
"""
Input: 2D list, where each inner list represents a student
       inner lists contain name, and the scores (variable length)
Output: 2D list, where each inner list contains student name and average grades.
"""
def process_student_grades(record):
    result=[]
    for grade in record:
        name=grade[0]
        sum=0
        for j in range (1,len(grade)):
            sum+=grade[j]
            avg=sum/j
        result.append([name,avg])
    return result

""" Test 3 """
def test_process_student_grades():
    print("Testing process_student_grades...", end='')

    assert(process_student_grades([
        ["Anu", 80, 90, 85],
        ["Ravi", 70, 75, 80]
    ]) == [
        ["Anu", 85.0],
        ["Ravi", 75.0]
    ])

    assert(process_student_grades([
        ["Meena", 100, 100, 100]
    ]) == [
        ["Meena", 100.0]
    ])

    assert(process_student_grades([
        ["Karthik", 50]
    ]) == [
        ["Karthik", 50.0]
    ])

    print("... done!")

if __name__ == '__main__':
    test_process_student_grades()
