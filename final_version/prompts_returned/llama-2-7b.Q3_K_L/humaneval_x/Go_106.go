 
// Implement the Function F that takes n as a parameter,
// and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
// or the sum of numbers from 1 to i otherwise.
// i starts from 1.
// the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
// Example:
// F(5) == [1, 2, 6, 24, 15]
func F(n int) []int {
    var ret []int
    for i := 0; i < n + 1; i++ { // start from 1 and not 0 for the first element
        ret = append(ret, i+1)
        if i%2 == 0 {
            for j := 0; j <= i/2; j++ {
                ret[i-j] = 1
            }
        } else {
            for j := 1; j < i; j++ {
                ret[i - j] = j
            }
        }
    }
    return ret
}
