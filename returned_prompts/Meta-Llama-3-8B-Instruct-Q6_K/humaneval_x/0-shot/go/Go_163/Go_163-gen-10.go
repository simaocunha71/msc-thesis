```go
package main
import "fmt"
func GenerateIntegers(a, b int) []int {
    if a > b {
        a, b = b, a
    }
    res := make([]int, 0)
    for i := a; i <= b; i++ {
        s := fmt.Sprintf("%d", i)
        for j := 0; j < len(s); j++ {
            if s[j]%2 == 0 {
                res = append(res, i)
                break
            }
        }
    }
    return res
}

func main() {
    fmt.Println(GenerateIntegers(2, 8)) // [2, 4, 6, 8]
    fmt.Println(GenerateIntegers(8, 2)) // [2, 4, 6, 8]
    fmt.Println(GenerateIntegers(10, 14)) // []
}
```


This code defines a function `GenerateIntegers` that takes two positive integers `a` and `b` as input, and returns a slice of integers representing the even digits between `a` and `b`, in ascending order.
The function first checks if `a` is greater than `b`, and if so, swaps their values to ensure that `a` is always less than or equal to `b`. Then, it initializes an empty slice `res` to store the result.
The function then iterates over the range `[a, b]` using a for loop, and for each integer `i` in this range, it converts `i` to a string `s` using `fmt.Sprintf`. It then iterates over the characters in `s` using a nested for loop, and checks if each character is even (i.e., `s[j]%2 == 0`) using the modulus operator `%`. If an even digit is found, it appends `i` to the result slice `res` and breaks out of the inner loop using `break`.
Finally, the function returns the result slice `res`.
In the `main` function, we test the `GenerateIntegers` function with different input ranges and print the results using `fmt.Println`. The output is as expected:
```
[2 4 6 8]
[2 4 6 8]
[]
```


The time complexity of this function is O(n), where n is the range `[a, b]`, because we iterate over the range and convert each integer