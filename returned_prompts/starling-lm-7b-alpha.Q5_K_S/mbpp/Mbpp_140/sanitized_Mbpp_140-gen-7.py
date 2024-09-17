def extract_singly(l):
    # your code here
    result = []
    for sub_list in l:
        for item in sub_list:
            result.append(item)
    return set(result)