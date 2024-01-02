
// Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
// Example
// IsEqualToSumEven(4) == false
// IsEqualToSumEven(6) == false
// IsEqualToSumEven(8) == true
func IsEqualToSumEven(n int) bool {
    var odd, even = 0, 0
    
	for a := 1; a <= n; a += 2 {
        if a % 2 != 0 {
            odd++
        } else {
            even++
        }
	}
	if odd == 4 || even == 4 {
		return true
	}
    
    return false
}