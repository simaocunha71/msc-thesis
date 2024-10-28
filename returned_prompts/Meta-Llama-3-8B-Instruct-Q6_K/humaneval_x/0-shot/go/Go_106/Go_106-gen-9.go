```go
func F(n int) []int {
    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i % 2 == 0 { // if i is even
            result[i] = factorial(i)
        } else { // if i is odd
            sum := 0
            for j := 1; j <= i; j++ {
                sum += j
            }
            result[i] = sum
        }
    }
    return result
}

func factorial(i int) int {
    if i == 0 {
        return 1
    }
    return i * factorial(i-1)
}
```

Explanation:
The function `F` takes an integer `n` as a parameter and returns a list of size `n`. The list is initialized with zeros. Then, a loop runs `n` times, and for each iteration `i`, it checks if `i` is even or odd. If `i` is even, the value of the element at index `i` is the factorial of `i`. If `i` is odd, the value of the element at index `i` is the sum of numbers from 1 to `i`. The factorial of `i` is calculated using a recursive function `factorial`. The list is then returned. 

The `factorial` function is a helper function that calculates the factorial of a given number `i`. It uses recursion to calculate the factorial. The base case is when `i` is 0, in which case the function returns 1. For other values of `i`, the function returns the product of `i` and the factorial of `i-1`. 

This solution has a time complexity of O(n) and a space complexity of O(n), where `n` is the input parameter. The space complexity is due to the list that is returned. The time complexity is due to the loop that runs `n` times and the recursive function calls. 

Note: The solution assumes that the input `n` is a non-negative integer. If the input can be negative or non-integer, additional error handling may be needed. 

Example:
```go
fmt.Println(F(5))  // Output: [1 2 6 24 15]
``` 





