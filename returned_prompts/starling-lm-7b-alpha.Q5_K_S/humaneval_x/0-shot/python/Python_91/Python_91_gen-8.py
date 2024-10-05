    # Your code here
    S = S.split(".")
    S = S.split("?")
    S = S.split("!")
    S = S.split()
    S = set(S)
    count = 0
    for i in S:
        if i.startswith('I'):
            count += 1
    return count

# def is_bored(S):
#     count = 0
#     for sentence in S.split(("." + "?!")):
#         if sentence.startswith('I'):
#             count += 1
#     return count

# def is_bored(S):
#     count = 0
#     for sentence in S.split(("." + "?" + "!")):
#         if sentence.startswith('I'):
#             count += 1
#     return count

# def is_bored(S):
#     count = 0
#     for i in S:
#         if i.startswith('I'):
#             count += 1
#     return count

































































































































































































































































