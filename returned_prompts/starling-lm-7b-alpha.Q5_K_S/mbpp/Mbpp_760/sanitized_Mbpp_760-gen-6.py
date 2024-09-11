from collections import Counter
def unique_Element(numList):
    count = Counter(numList)
    if len(count) == 1:
        return True
    else:
        return False