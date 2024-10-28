
def find_first_occurrence(nums, target):
    try:
        return nums.index(target)
    except ValueError:
        return -1


