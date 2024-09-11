def number_of_substrings(string):
    length = len(string)
    if length == 0:
        return 0
    else:
        count = 0
        for i in range(length):
            for j in range(i+1, length+1):
                count += 1
        return count

# assert number_of_substrings("abc") == 6

def number_of_substrings(string):
    length = len(string)
    if length == 0:
        return 0
    else:
        count = 0
        for i in range(length):
            for j in range(i+1, length+1):
                count += 1
        return count

print(number_of_substrings("abc"))


# Here are some of the test cases

# print(number_of_substrings("")) # 1
# print(number_of_substrings("a")) # 2
# print(number_of_substrings("ab")) # 3
# print(number_of_substrings("abc")) # 6
# print(number_of_substrings("abcdef")) # 10
# print(number_of_substrings("abcdefg")) # 15
# print(number_of_substrings("abcdefgh")) # 21
# print(number_of_substrings("abcdefghi")) # 28
# print(number_of_substrings("abcdefghij")) # 36
# print(number_of_substrings("abcdefghijkl")) # 45
# print(number_of_substrings("abcdefghijklm")) # 55
# print(number_of_substrings("abcdefghijklmn")) # 66
# print(number_of_substrings("abcdefghijklmno")) # 78
# print(number_of_substrings("abcdefghijklmnop")) # 91
# print(number_of_substrings("abcdefghijklmnopq")) # 105
# print(number_of_substrings("abcdefghijklmnopqr")) #