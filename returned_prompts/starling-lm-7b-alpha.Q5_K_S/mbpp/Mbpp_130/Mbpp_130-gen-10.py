def max_occurrences(nums):
    return max(nums, key = nums.count)

# The above function uses built-in max() function, which is not efficient for large inputs. Here is a better solution using dictionary.

def max_occurrences_dict(nums):
    counter = {}
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    return max(counter, key = counter.get)


# Testing the function
import unittest
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]), 2)
        self.assertEqual(max_occurrences_dict([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]), 2)
if __name__ == '__main__':
    unittest.main()














"""
def max_occurrences(nums):
    max_val = nums[0]
    max_count = 1
    for num in nums:
        if num == max_val:
            max_count += 1
        elif max_count < 1:
            max_val = num
            max_count = 1
        else:
            max_val = num
            max_count = 1
    return (max_val, max_count)

# Testing the function
def test_max_occurrences():
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]) == (2, 4)
    assert max_occurrences_dict([2,3,8