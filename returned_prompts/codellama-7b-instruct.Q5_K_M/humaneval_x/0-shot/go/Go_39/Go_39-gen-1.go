	if n <= 0 {
		return 0
	}

	fib := int(math.Sqrt(float64(n)))
	for {
		for i := 0; i < n; i++ {
			if i == 0 {
				if fib == 1 {
					return 2
				}
				fib--
			} else {
				fib = int(math.Sqrt(float64(i*i + fib*fib)))
				if fib == 1 {
					return i + 1
				}
			}
		}
		if fib < 0 {
			break
		}
	}
	return 0
}

// isPrime checks if the given number is prime.
// >>> isPrime(1)
// false
// >>> isPrime(2)
// true
// >>> isPrime(3)
// true
// >>> isPrime(4)
// false
// >>> isPrime(5)
// true
func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(PrimeFib(1))
	fmt.Println(PrimeFib(2))
	fmt.Println(PrimeFib(3))
	fmt.Println(PrimeFib(4))
	fmt.Println(PrimeFib(5))
}
