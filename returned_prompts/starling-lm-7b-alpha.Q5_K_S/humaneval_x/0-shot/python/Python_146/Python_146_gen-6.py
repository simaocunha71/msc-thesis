    def specialFilter(nums):
        count = 0
        for n in nums:
            first = int(str(n)[0])
            last = int(str(n)[-1])
            if first % 2 != 0 and last % 2 != 0 and n > 10:
                count += 1
        return count

    return specialFilter(nums)




































# Explanation:

# In this problem, we are asked to write a function that takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and both the first and last digits of a number are odd (1, 3, 5, 7, 9).

# To solve this problem, we first initialize a variable called 'count' to keep track of the number of elements that meet the criteria. We then iterate through each number in the input array. For each number, we convert it to a string and extract the first and last digits. If the first and last digits are both odd and the number is greater than 10, we increment the 'count' variable by 1. Finally, we return the 'count' variable as the result.

# For example, if we have the input array [15, -73, 14, -15], the first number 15 is not greater than 10, so we move on to the next number -73. The first digit of -73 is 7 and the last digit is 3, which are both odd. Therefore, we increment the 'count' variable by 1. We continue this process for all the numbers in the array until we reach the end. In the end, the 'count' variable will hold the number of elements that meet the criteria, which is 1 in this case.

# Similarly, if we have the input array [33, -2, -3, 45, 21, 109], the first number 33 is greater than 10 and both the first and last digits are odd. Therefore, we increment the 'count' variable by 1. The