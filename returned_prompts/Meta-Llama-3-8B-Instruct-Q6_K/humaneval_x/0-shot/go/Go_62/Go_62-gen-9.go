```
func Derivative(xs []int) []int {
    result := make([]int, len(xs)-1)
    for i := 1; i < len(xs); i++ {
        result[i-1] = xs[i] * i
    }
    return result
}
```
The function Derivative takes as input a slice of integers xs representing the coefficients of a polynomial, and returns a new slice representing the derivative of that polynomial.

The derivative of a polynomial is calculated by multiplying each coefficient by its corresponding power of x, and shifting the resulting coefficients one position to the left. This is implemented in the function by iterating over the coefficients starting from the second one, multiplying each one by its index, and storing the results in a new slice.

For example, if the input is [3, 1, 2, 4, 5], the function will return [1, 4, 12, 20], which are the coefficients of the derivative polynomial 1 + 4x + 12x^2 + 20x^3. If the input is [1, 2, 3], the function will return [2, 6], which are the coefficients of the derivative polynomial 2 + 6x.