To solve this problem, we can use a nested loop to compare every pair of elements in the array. Then, we can check if the sum of each pair is present in the array and if it is zero.

Here's a step-by-step breakdown of the solution:

1. First, we sort the input array in ascending order using the `sort` method. This step is not essential but it can help reduce the number of elements to check, especially for larger arrays.

2. Next, we use two nested loops to compare every pair of elements in the array. The outer loop iterates over the first element of the pair, while the inner loop iterates over the second element. We start both loops from index 1 to ensure that we don't compare the same element with itself.

3. Inside the inner loop, we check if the sum of the current pair is equal to zero. If it is, we check if the pair is distinct (i.e., if the indices of the elements in the pair are different). If the pair is distinct, we return true.

4. If the sum of the current pair is not zero, we continue to the next iteration of the inner loop. If we finish the inner loop without finding a distinct pair that sums to zero, we continue to the next iteration of the outer loop.

5. If we finish all iterations of both loops without finding a distinct pair that sums to zero, we return false.

Here's the code that implements the above solution:

```python
def triplesSumToZero(l):
    l.sort()
    for i in range(len(l) - 2):
        for j in range(i + 1, len(l) - 1):
            if l[i] + l[j] == 0 and i != j:
                return True
    return False
```

You can test the function with the provided test cases to verify its correctness:

```python
print(triplesSumToZero([1, 3, 5, 0]))  # Expected output: False
print(triplesSumToZero([1, 3, -2, 1]))  # Expected output: True
print(triplesSumToZero([1, 2, 3, 7])) 