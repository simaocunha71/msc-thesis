```go
func F(n int) []int {
    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i % 2 == 0 {
            result[i] = factorial(i)
        } else {
            sum := 0
            for j := 1; j <= i; j++ {
                sum += j
            }
            result[i] = sum
        }
    }
    return result
}

func factorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * factorial(n-1)
}
```
Explanation:
The function `F` takes an integer `n` as input and returns a list of size `n`. It iterates through the list and for each element at index `i`, it checks if `i` is even. If `i` is even, it calculates the factorial of `i` using the `factorial` function and stores it in the result list. If `i` is odd, it calculates the sum of numbers from 1 to `i` and stores it in the result list.

The `factorial` function is a recursive function that calculates the factorial of a given number `n`. It returns `1` if `n` is `0`, and otherwise, it returns `n` multiplied by the factorial of `n-1`.

For example, if we call `F(5)`, it will return the list `[1, 2, 6, 24, 15]`. The element at index `0` is `1`, the element at index `1` is `2`, the element at index `2` is `6` (which is the factorial of `2`), the element at index `3` is `24` (which is the factorial of `4`), and the element at index `4` is `15` (which is the sum of numbers from `1` to `4`).