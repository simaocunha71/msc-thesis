```go
func StartsOneEnds(n int) int {
    count := 0
    for i := 1; i < 10; i++ {
        if i == 1 {
            count++
        }
        num := int(math.Pow10(n-1)) + i
        if num%10 == 1 {
            count++
        }
    }
    return count
}
```
The function `StartsOneEnds` takes an integer `n` as input and returns the count of the numbers of `n`-digit positive integers that start or end with 1.

Here's a simple and efficient solution:
1. Initialize a counter `count` to 0.
2. Loop through all single-digit numbers from 1 to 9.
3. If the current single-digit number is 1, increment the counter.
4. Calculate the `n`-digit number by adding the current single-digit number to the result of `10^(n-1)`.
5. Check if the last digit of the `n`-digit number is 1. If it is, increment the counter.
6. Return the total count.

The time complexity of this solution is O(1), as it only depends on the input `n` and does not rely on any external data structures or algorithms with a varying time complexity. The space complexity is O(1) as well, as it only uses a constant amount of space to store the counter and the loop variables.