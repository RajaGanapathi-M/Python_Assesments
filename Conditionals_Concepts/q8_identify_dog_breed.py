""" Question 8: identify_dog_breed """
"""
Inputs: weight (integer) and coat_length (string)
Output: corresponding dog breed (see Workbook for table)
"""
def identify_dog_breed(weight, coat_length):
    if weight<20:
        if coat_length=="medium":
            return "Mudi"
        elif coat_length=="short":
            return "Swedish Vallhud"
        else:
            return "Shetland Sheepdog"
    elif weight>20 and weight<=50:
        if coat_length=="short":
            return "Pembroke Welsh Corgi"
        elif coat_length=="medium":
            return "Australian Shepherd"
        else :
            return "Collie"
    elif weight<50 and weight>=80:
        if coat_length=="short":
            return "Belgian Maliniois"
        elif coat_length=="long":
            return "collie"
        else :
            return " Bearded Collie"
    else:
        if coat_length=="short":
            return "Beaucern"
        elif coat_length=="medium":
            return "Bouvier des Flandres" 
        else:
            return "Old English Sheepdog"
  

""" Test 8 """
def test_identify_dog_breed():
    print("Testing identify_dog_breed...", end="")
    assert(identify_dog_breed(25, "short") == "Pembroke Welsh Corgi")
    assert(identify_dog_breed(95, "long") == "Old English Sheepdog")
    assert(identify_dog_breed(19, "medium") == "Mudi")
    assert(identify_dog_breed(50, "long") == "Collie")
    print("... done!")

if __name__ == '__main__':
    test_identify_dog_breed()