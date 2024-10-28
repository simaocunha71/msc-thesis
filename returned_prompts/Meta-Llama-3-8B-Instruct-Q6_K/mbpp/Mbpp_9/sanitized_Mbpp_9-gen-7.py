def find_Rotations(s):
    return len(s) // len(set(s)) if len(set(s)) > 1 else 0