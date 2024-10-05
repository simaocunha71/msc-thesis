
// Write a function that returns true if the given number is the multiplication of 3 prime numbers
// and false otherwise.
// Knowing that (a) is less then 100.
// Example:
// IsMultiplyPrime(30) == true
// 30 = 2 * 3 * 5
func IsMultiplyPrime(a int) bool {

	var prime = func(n int) bool {
		for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
			if n%i == 0 {
				return false
			}
		}
		return true
	}
	for i := 2; i < 10; i++ {
		if prime(i) {
			for j := 2; j < 10; j++ {
				if prime(j) {
					for k := 2; k < 10; k++ {
						if prime(k) {
							if a == i*j*k {
								return true
							}
						}
					}
				}
			}
		}
	}
	return false
}
