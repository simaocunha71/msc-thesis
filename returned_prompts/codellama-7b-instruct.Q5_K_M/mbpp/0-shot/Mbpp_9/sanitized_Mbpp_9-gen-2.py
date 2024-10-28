def find_Rotations(str1):
    count = 0
    while str1 != str1[len(str1)-1:len(str1)] + str1[0:len(str1)-1]:
        count += 1
        str1 = str1[1:len(str1)] + str1[0:1]
    return count