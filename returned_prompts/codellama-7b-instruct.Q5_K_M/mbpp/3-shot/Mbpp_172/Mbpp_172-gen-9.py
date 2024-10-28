
def count_occurance(string: str) -> int:
    count = 0
    for i in range(len(string)-3):
        if string[i:i+3] == 'std':
            count += 1
    return count


