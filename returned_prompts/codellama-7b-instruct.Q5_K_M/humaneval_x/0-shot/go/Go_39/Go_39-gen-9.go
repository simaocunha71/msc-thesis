	if n < 1 {
		return -1
	}

	if n == 1 {
		return 2
	}

	if n == 2 {
		return 3
	}

	if n == 3 {
		return 5
	}

	i := 0
	f := 0
	for {
		i++
		f = Fib(i)
		if IsPrime(f) {
			if i == n {
				break A
			}
		}
	}
	return f
}

func Fib(i int) int {
	if i == 0 {
		return 0
	}
	if i == 1 {
		return 1
	}
	return Fib(i-1) + Fib(i-2)
}

func IsPrime(x int) bool {
	if x <= 1 {
		return false
	}
	if x == 2 || x == 3 {
		return true
	}
	if x%2 == 0 || x%3 == 0 {
		return false
	}
	for i := 5; i*i <= x; i += 6 {
		if x%i == 0 || x%(i+2) == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(PrimeFib(5))
}

