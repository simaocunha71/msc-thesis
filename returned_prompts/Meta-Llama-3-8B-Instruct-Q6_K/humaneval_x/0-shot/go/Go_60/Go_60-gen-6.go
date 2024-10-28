Your solution goes here. Do not forget to return the result.
```go
func SumToN(n int) int {
    sum := 0
    for i := 1; i <= n; i++ {
        sum += i
    }
    return sum
}
```



Here is the explanation:

This function, `SumToN`, takes an integer `n` as input and returns the sum of all numbers from 1 to `n`.

The function uses a `for` loop to iterate from 1 to `n` and adds each number to a running total `sum`. The loop starts from 1 and continues until the condition `i <= n` is met, at which point `i` is incremented by 1 until `i` exceeds `n`. The sum is then returned at the end of the function.

The time complexity of this function is O(n), which means it takes linear time to calculate the sum for a given input `n`. The space complexity is O(1), which means it uses constant space to store the sum and the loop variable `i`. This function can be used to calculate the sum of numbers from 1 to a given number `n`.