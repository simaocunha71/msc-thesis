def count_Substrings(string):
    def get_sum(string):
        return sum(int(i) for i in string)
    count = 0
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            sub_string = string[i:j]
            if get_sum(sub_string) == len(sub_string):
                count += 1
    return count