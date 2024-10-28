
// using a stack, we will push every "<" into the stack and every ">" we will pop from the stack.
// if the stack is empty at the end, return true, otherwise return false.

    var stack []rune
    for _, c := range brackets {
        if c == '<' {
            stack = append(stack, c) 
        } else {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}

```

The solution to the problem is to use a stack data structure.

We iterate over the string, pushing every '<' into the stack. When we encounter a '>', we pop from the stack. If the stack is empty (meaning there is no matching '<' for the '>'), we return false. If the stack is not empty at the end (meaning there are unmatched '<'s), we return false. If we haven't returned false by this point, the bracketing is correct, so we return true.

This solution has a time complexity of O(n), where n is the length of the string.

It uses O(n) extra space for the stack.

The space complexity could be reduced to O(1) by not using an explicit stack. Instead, you could keep track of the number of unmatched '<'s and return false as soon as you encounter a '>' without a corresponding '<'. However, this would complicate the code.


# Question 2

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

```python
def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if