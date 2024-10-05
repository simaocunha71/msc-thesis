def is_bored(S):
    return sum(S[i].startswith("I") for i in range(len(S)) if S[i][-1] in "!?.")