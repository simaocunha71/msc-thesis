    var fibs []int = []int{0, 1}
    for i := 2; i <= 1000; i++ {
        fibs = append(fibs, fibs[i-1]+fibs[i-2])
    }

    prime_fibs := []int{}
    for _, fib := range fibs {
        if fib > 1 {
            is_prime := true
            for i := 2; i <= math.Sqrt(float64(fib)); i++ {
                if fib%i == 0 {
                    is_prime = false
                    break
                }
            }
            if is_prime {
                prime_fibs = append(prime_fibs, fib)
            }
        }
    }
    return prime_fibs[n-1]
}

