Here is the solution in Go:
```go
func IsSimplePower(x int, n int) bool {
    for i := 1; i <= x; i++ {
        if int(math.Pow(float64(n), float64(i))) == x {
            return true
        }
    }
    return false
}
```
Here's an explanation of the code:
* The function takes two integers `x` and `n` as input.
* The function uses a for loop to iterate from 1 to `x`.
* In each iteration, it checks if `n` raised to the power of `i` is equal to `x`. This is done using the `math.Pow` function from the Go standard library, which returns the value of `n` raised to the power of `i`.
* If the condition is true, the function returns `true`.
* If the loop completes without finding a match, the function returns `false`.

You can test this function with the examples you provided:
```go
fmt.Println(IsSimplePower(1, 4)) // true
fmt.Println(IsSimplePower(2, 2)) // true
fmt.Println(IsSimplePower(8, 2)) // true
fmt.Println(IsSimplePower(3, 2)) // false
fmt.Println(IsSimplePower(3, 1)) // false
fmt.Println(IsSimplePower(5, 3)) // false
``` 