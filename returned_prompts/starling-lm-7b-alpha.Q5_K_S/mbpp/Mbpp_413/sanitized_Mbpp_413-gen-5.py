def extract_nth_element(lst, n):
    extracted = []
    for i in range(len(lst)):
        if i == n:
            extracted.append(lst[i][0])
    return extracted