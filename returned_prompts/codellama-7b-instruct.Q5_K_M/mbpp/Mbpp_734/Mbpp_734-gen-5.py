```python
def sum_Of_Subarray_Prod(arr):
  # Initialize the result
  result = 0

  # Traverse the given list
  for i in range(len(arr)):
      # Sum of products of sublist starting from 0 to i
      result += sum(arr[0:i+1])

  # Return the result
  return result
```
