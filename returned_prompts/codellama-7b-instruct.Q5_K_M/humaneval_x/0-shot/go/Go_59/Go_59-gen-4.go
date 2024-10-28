
// Return the largest prime factor of n. Assume n > 1 and is not a prime.
// >>> LargestPrimeFactor(13195)
// 29
// >>> LargestPrimeFactor(2048)
// 2
func LargestPrimeFactor(n int) int {
	for n%2 == 0 {
		n /= 2
	}
	for n%3 == 0 {
		n /= 3
	}
	for n%5 == 0 {
		n /= 5
	}
	for n%7 == 0 {
		n /= 7
	}
	for n%11 == 0 {
		n /= 11
	}
	for n%13 == 0 {
		n /= 13
	}
	for n%17 == 0 {
		n /= 17
	}
	for n%19 == 0 {
		n /= 19
	}
	for n%23 == 0 {
		n /= 23
	}
	for n%29 == 0 {
		n /= 29
	}
	return n
}

func main() {
	fmt.Println(LargestPrimeFactor(13195))
}

// https://play.golang.org/p/03_ZjwB4vV

