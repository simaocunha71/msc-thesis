def find_even_pair(lst):
    return sum(1 for i in range(len(lst)) for j in range(i+1, len(lst)) if (i ^ j) % 2 == 0) // 2