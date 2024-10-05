  We can solve this problem by using a hashmap. The idea is to traverse the array and for every element, we check if it's complement (target - element) is present in the hashmap. If present, we return the indices. If not, we insert the element in the hashmap.

  Here is the Python code:

  ```python
  def twoSum(nums, target):
      hashmap = {}
      for i, num in enumerate(nums):
          complement = target - num
          if complement in hashmap:
              return [hashmap[complement], i]
          hashmap[num] = i
      return []
  ```

  The time complexity of this solution is O(n) because we traverse the array once. The space complexity is O(n) because in the worst case, we insert all elements into the hashmap.
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```
  ```