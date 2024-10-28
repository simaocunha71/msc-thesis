
def change_base(x: int, base: int):
    # 1. convert to a string
    s = str(x)
    # 2. make an empty string to store the result
    result = ""
    # 3. iterate over each digit of the string
    for digit in s:
        # 4. convert each digit from base 10 to base
        result += str(int(digit) % base)
    # 5. return the result
    return result

