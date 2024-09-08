def multiple_to_single(lst):
    return int(''.join(map(str, lst)))

print(multiple_to_single([11, 33, 50])) # 113350

