        List<String> result = new ArrayList<>();
        Stack<Character> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                stack.push(c);
                sb.append(c);
            } else if (c == ')') {
                stack.pop();
                sb.append(c);
                if (stack.isEmpty()) {
                    result.add(sb.toString());
                    sb.setLength(0);
                }
            }
        }

        return result;
    }
}

```

## 20. Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3.

It doesn't matter what values are set beyond the returned length.

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;
        for (int n : nums)
            if (i < 2 || n > nums[i-2])
                nums[i++] = n;
        return i;
    }
}
```

## 21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be