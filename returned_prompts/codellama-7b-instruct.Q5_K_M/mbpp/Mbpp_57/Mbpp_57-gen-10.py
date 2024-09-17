
def find_Max_Num(digits):
    def is_num_valid(num):
        if num < 10**(len(digits)-1):
            return False
        for i in range(1, len(digits)):
            if num % 10**i != digits[i]:
                return False
        return True

    max_num = -1
    for i in range(len(digits)):
        for j in range(i, len(digits)):
            num = digits[i] * 10**(j-i) + digits[j]
            if is_num_valid(num):
                max_num = max(max_num, num)
    return max_num


