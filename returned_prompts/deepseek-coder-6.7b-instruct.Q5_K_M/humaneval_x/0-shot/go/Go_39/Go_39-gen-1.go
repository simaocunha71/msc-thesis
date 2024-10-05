	i := 2
	j := 0
	k := 0
	l := 0

	prime := make([]int, 50)
	fib := make([]int, 50)
	
B:
	fib[0] = 1
	fib[1] = 2
	prime[0] = 2
	j = 2
	
C:
	for i = 3; i <= 100; i++ {
		l = 0
		for j = 1; j < len(prime); j++ {
			if i%prime[j] == 0 {
				l = 1
				break
			}
		}
		if l == 0 {
			prime[j] = i
			j++
		}
	}
	
D:
	fib[0] = 1
	fib[1] = 2
	k = 2
	
E:
	for k < 50 {
		fib[k] = fib[k-1] + fib[k-2]
		l = 0
		for j = 0; j < len(prime); j++ {
			if fib[k] == prime[j] {
				l = 1
				break
			}
		}
		if l == 0 {
			k++
		} else {
			fib[k] = 0
			k++
		}
	}
	
G:
	for n > 0 {
		for i = 0; i < len(fib); i++ {
			if fib[i] != 0 {
				n--
				if n == 0 {
					return fib[i]
				}
			}
		}
	}
	
	return 0
}












































































































