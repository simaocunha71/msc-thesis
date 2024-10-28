
def find_Rotations(str):
    return len(str) - len(set(''.join(sorted(str))))


