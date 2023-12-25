
// Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
// Example
// IsEqualToSumEven(4) == false
// IsEqualToSumEven(6) == false
// IsEqualToSumEven(8) == true
func IsEqualToSumEven(n int) bool {
    var result = 0
    for i := 2; ; ++i {
        if (i & 3) != 1 && even(result+i) > n {
            return false
        } else if even(result+i) == n {
            break
        }
    }
}
