
// Implement the Function F that takes n as a parameter,
// and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
// or the sum of numbers from 1 to i otherwise.
// i starts from 1.
// the factorial of i is the multiplication of the numbers from 1 to i  (1 * 2 * ... * i).
// Example:
// F(5) == [1, 2, 6, 24, 15]

// Define the F function
func F(n int) []int {

    // Initialize an array of size n
    result := make([]int, n)

    // Loop through the array
    for i := range result {

        // If i is even, calculate the factorial of i
        if (i+1)%2 == 0 {
            result[i] = factorial(i+1)
        } else { // If i is odd, calculate the sum of numbers from 1 to i
            result[i] = sum(i+1)
        }
    }

    // Return the result
    return result
}

// Define the factorial function
func factorial(n int) int {

    // Initialize the factorial
    fact := 1

    // Calculate the factorial
