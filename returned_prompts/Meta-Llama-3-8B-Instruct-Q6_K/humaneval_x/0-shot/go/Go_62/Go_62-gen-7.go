```
func Derivative(xs []int) []int {
    result := make([]int, len(xs)-1)
    for i := 1; i < len(xs); i++ {
        result[i-1] = xs[i] * i
    }
    return result
}
```



The Derivative function calculates the derivative of a polynomial represented as an array of coefficients. The derivative of a polynomial is calculated by multiplying each coefficient of the polynomial by its corresponding power of x and decreasing the power by 1.

Here's how the function works:
- It creates a new array `result` with a length one less than the input array `xs`.
- It then iterates over the input array `xs`, starting from the second element (at index 1), and calculates the derivative of each element.
- For each element, it multiplies the element by its index (which is the power of x) and stores the result in the corresponding index of the `result` array.
- Finally, it returns the `result` array, which represents the derivative of the input polynomial.

For example, if the input array is `[3, 1, 2, 4, 5]`, the function will return `[1, 4, 12, 20]`, which are the coefficients of the derivative polynomial `1x + 4x^2 + 12x^3 + 20x^4`. If the input array is `[1, 2, 3]`, the function will return `[2, 6]`, which are the coefficients of the derivative polynomial `2x + 6x^2`.