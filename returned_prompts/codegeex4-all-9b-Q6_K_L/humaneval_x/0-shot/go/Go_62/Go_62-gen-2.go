You can solve this problem by iterating over the coefficients of the polynomial and calculating the derivative of each coefficient. The derivative of a coefficient xs[i] is given by xs[i+1] * (i+1). Here's how you can implement this in Go:

```go
func Derivative(xs []int) []int {
    n := len(xs)
    der := make([]int, n-1)
    for i := 1; i < n; i++ {
        der[i-1] = xs[i] * i
    }
    return der
}
```

This function takes a slice of integers `xs` as input and returns a new slice `der` containing the coefficients of the derivative of the polynomial. The function first calculates the length of the input slice `xs` and creates a new slice `der` of length `n-1` where `n` is the length of `xs`. Then, it iterates over the coefficients of `xs` starting from the second coefficient (index 1) and calculates the derivative of each coefficient using the formula `xs[i] * i` and stores it in the corresponding position of `der`. Finally, it returns the derivative `der`.

Here's an example usage of the function:

```go
func main() {
    xs := []int{3, 1, 2, 4, 5}
    der := Derivative(xs)
    fmt.Println(der) // Output: [1, 4, 12, 20]
}
```

This will output the derivative of the polynomial `[3, 1, 2, 4, 5]` which is `[1, 4, 12, 20]`.