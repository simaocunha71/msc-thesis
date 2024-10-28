    fib_nums := make([]int, n + 1)
    fib_nums[0] = 0
    fib_nums[1] = 1

    for i := 2; i <= n; i++ {
        fib_nums[i] = fib_nums[i-1] + fib_nums[i-2]
        if fib_nums[i] > n {
            break
        }
    }

    for _, fib_num := range fib_nums {
        if fib_num > n {
            break
        }
        if fib_num > 2 && is_prime(fib_num) {
            return fib_num
        }
    }
    return -1
}


func is_prime(n int) bool {
    if n == 2 || n == 3 {
        return true
    }

    if n < 2 || n%2 == 0 {
        return false
    }

    limit := int(math.Sqrt(float64(n)))
    for i := 3; i <= limit; i += 2 {
        if n%i == 0 {
            return false
        }
    }
    return true
}



