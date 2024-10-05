
def is_bored(S):
    i = 0
    while i < len(S):
        if S[i] == "I":
            if S[i+1] == ".":
                return 1
            elif S[i+1] == "?":
                return 1
            elif S[i+1] == "!":
                return 1
        i += 1
    return 0

