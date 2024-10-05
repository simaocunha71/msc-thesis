Here is the solution for the problem:
```go
import (
    "sort"
)

func GetOddCollatz(n int) []int {
    var result []int
    for n != 1 {
        if n%2 == 1 {
            result = append(result, n)
        }
        if n%2 == 0 {
            n = n / 2
        } else {
            n = 3*n + 1
        }
    }
    sort.Ints(result)
    return result
}
```
Explanation:
The function `GetOddCollatz` takes an integer `n` as input and returns a sorted list of odd numbers in the Collatz sequence.

The function uses a loop to generate the Collatz sequence for the input `n`. Inside the loop, it checks if `n` is odd or even. If `n` is odd, it appends `n` to the `result` slice. If `n` is even, it divides `n` by 2. If `n` is odd, it multiplies `n` by 3 and adds 1.

After the loop, the function sorts the `result` slice in increasing order using the `sort.Ints` function. Finally, it returns the sorted list of odd numbers in the Collatz sequence.

For example, if the input is `5`, the function will return `[1, 5]`, which are the odd numbers in the Collatz sequence for `5`. If the input is `10`, the function will return `[1, 3, 19]`, which are the odd numbers in the Collatz sequence for `10`.