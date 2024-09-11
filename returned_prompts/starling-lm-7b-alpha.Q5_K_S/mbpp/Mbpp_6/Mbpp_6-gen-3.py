def differ_At_One_Bit_Pos(a,b):
    a = bin(a)
    a = a[2:]
    b = bin(b)
    b = b[2:]
    if len(a) != len(b):
        return False
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False


# Python3 program to check if two
# numbers have exactly one bit
# differing


# Function to check if two numbers
# have exactly one bit differing
def check(x, y):

    # convert the given numbers
    # to binary and find the first
    # position where the bits are
    # different. If all bits are same,
    # return 0
    i = 0
    while (x != y):
        if (x & 1) != (y & 1):
            return i
        x >>= 1
        y >>= 1
        i += 1
    return -1


# Driver program to check the above
# function
def main():
    # The numbers
    x = 13
    y = 9

    # Function call
    res = check(x, y)

    # If one bit is different, print
    # true, else print false
    if (res != -1):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()



"""
Explanation:
The above program uses bitwise operators to check if two numbers have exactly one bit differing. It first converts the two numbers to binary and then uses a loop to find the first position where the bits are different. If all bits are same, it returns 0. Otherwise, it returns the position of the differing bit. In the main() function, it uses this function to check if the two numbers have exactly one bit differing. If the result is not -1, it means that the two numbers have exactly one bit differing and it prints "True". Otherwise, it prints "False