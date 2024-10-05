    if len(set(lst)) != len(lst):
        return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))  # Check if each element is less than or equal to the next one


