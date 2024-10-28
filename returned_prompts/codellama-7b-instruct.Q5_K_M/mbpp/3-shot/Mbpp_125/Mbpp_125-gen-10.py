
def find_length(binary_str: str) -> int:
    count = 0
    for i in binary_str:
        if i == '0':
            count += 1
        else:
            count = 0
        if count > 1:
            return count
    return count


