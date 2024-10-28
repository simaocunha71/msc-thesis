 
// Implement the Function F that takes n as a parameter,
// and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
// or the sum of numbers from 1 to i otherwise.
// i starts from 1.
// the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
// Example:
// F(5) == [1, 2, 6, 24, 15]
func F(n int) []int {
    var result = make([]int, n)
    for i := 1; i < n; i++ {
        if i%2 == 0 {
            result[i] = Factorial(i)
        } else {
            result[i] = Sum(1, i)
        }
    }
    return result
}

// Implement the Function Factorial that takes one parameter n,
// and returns the factorial of n.
func Factorial(n int) int {
    var result = 1
    for i := 1; i <= n; i++ {
        result *= i
    }
    return result
}

// Implement the Function Sum that takes two parameters start and end,
// and returns the sum of numbers from start to end (inclusive).
func Sum(start, end int) int {
    var result = 0
    for i := start; i <= end; i++ {
        result += i
    }
    return result
}
