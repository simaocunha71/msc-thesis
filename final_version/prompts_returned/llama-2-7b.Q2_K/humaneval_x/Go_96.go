
// Implement a function that takes an non-negative integer and returns an array of the first n
// integers that are prime numbers and less than n.
// for example:
// CountUpTo(5) => [2,3]
// CountUpTo(11) => [2,3,5,7]
// CountUpTo(0) => []
// CountUpTo(20) => [2,3,5,7,11,13,17,19]
// CountUpTo(1) => []
// CountUpTo(18) => [2,3,5,7,11,13,17]
func CountUpTo(n int) []int {
	if n == 0 || n < 0 {
		return nil
	}

	res := make([]int, 0, len(primes)+1)
	candidates := primes[1:]
	for i := range candidates {
		if i+1 >= n {
			break
		} else if !isPrime(int64(i+1)) {
			res = append(res, int64(i+1))
			candidates[i] = nil // remove from candidates so that we don't keep iterating with i >= n
		}
	}

	return res
}