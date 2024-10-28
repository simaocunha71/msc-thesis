    # define the original numbers
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    # define the minimum and maximum of the original numbers
    min_num = min(numbers)
    max_num = max(numbers)
    # apply the transform to each number in the list
    rescaled_numbers = [(x - min_num) / (max_num - min_num) for x in numbers]
    return rescaled_numbers






# Python3 program to reshape the array
# according to the given
# condition

# Function to reshape the array
def rescaleToUnit(nums):
    # Finding Minimum and maximum in the array
    min_num = min(nums)
    max_num = max(nums)

    # Transforming the array elements
    res = [(nums[i] - min_num)/(max_num - min_num) for i in range(len(nums))]
    return res


# Driver code
if __name__ == "__main__":
    nums = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(rescaleToUnit(nums))










































































































































































































