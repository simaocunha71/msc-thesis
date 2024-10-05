	f := []int{0, 1}
	for i := 2; i <= n; i++ {
		f = append(f, f[i-1]+f[i-2])
		for j := 2; j*j <= f[i]; j++ {
			if f[i]%j == 0 {
				break
			}
			if j*j > f[i] {
				return f[i]
			}
		}
	}
	return 0
}




/*

A Fibonacci prime is a Fibonacci number that is also a prime number. The first few Fibonacci primes are: 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 601, 987, 1597, 2584, 4181, 6706, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, ...

To find the nth Fibonacci prime, you can start