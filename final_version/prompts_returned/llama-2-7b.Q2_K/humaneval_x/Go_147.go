
// You are given a positive integer n. You have to create an integer array a of length n.
// For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
// Return the number of triples (a[i], a[j], a[k]) of a where i < j < k,
// and a[i] + a[j] + a[k] is a multiple of 3.
// 
// Example :
// Input: n = 5
// Output: 1
// Explanation:
// a = [1, 3, 7, 13, 21]
// The only valid triple is (1, 7, 13).
func GetMaxTriples(n int) int {
	if n <= 0 || n == 1 {
		return 0
	} else if !(n&1) && n % 3 != 0 { // if number is odd and is not a multiple of three, return zero.
		return 0
	} else if (n-1)%3 > 0 { // if first triple does not exist add 1 to the result
		return GetMaxTriples(n - 1) + 1
	} else {
		result := 0
		maxDivisor := n
		for ; maxDivisor >= 3; maxDivisor -= 2 { // add all divisors of the number to the result.
			divisor := (n - 1) / maxDivisor + 1
			if divisor > 0 && divisor*maxDivisor >= n {
				result += divisor
			}
		}
		return result
	}
}