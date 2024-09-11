def two_unique_nums(nums):
    nums.sort()
    unique_nums = []
    prev_num = None

    for num in nums:
        if num != prev_num:
            unique_nums.append(num)
            prev_num = num

    return unique_nums


# Python3 program to remove duplicate elements
# from the given list.

# Function to remove duplicate
# elements from the given list
def remove_duplicates(list1):

    # Iterate through the given list
    for i in range(len(list1)):
        # Iterate from i+1 to the end of the list
        for j in range(i + 1, len(list1)):

            # If any element is found to be same
            # then that element is removed from the list
            if list1[i] == list1[j]:
                del list1[j]

    return list1

# Driver Code
if __name__ == "__main__":
    list1 = [1, 2, 3, 2, 3, 4, 5]
    print(remove_duplicates(list1))

# This code is contributed by PrinciRaj15

def remove_duplicates_from_list(list1):
    list1.sort()
    prev_num = None
    unique_nums = []
    for num in list1:
        if num != prev_num:
            unique_nums.append(num)
            prev_num = num
    return unique_nums

# Python3 program to remove duplicate
# elements from the given list.

# Function to remove duplicate
# elements from the given list
def remove_duplicates(list1):

    # Iterate through the given list
    for i in range(len(list1)):
        # Iterate from i+1 to the end of the list
        for j in range(i + 1, len(list1)):

            # If any element is found to be same
            # then that element is removed from the list
            if list1[i] == list1[j]:
                del list