import sys
def check_tuplex(tuplex, elem):
    for i in range(len(tuplex)):
        if (tuplex[i] == elem):
            return True
    return False