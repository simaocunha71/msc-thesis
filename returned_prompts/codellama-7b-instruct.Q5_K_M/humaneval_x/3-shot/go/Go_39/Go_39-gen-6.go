    fib_nums := []int{1, 1}
    for i := 2; i < n; i++ {
        fib_nums = append(fib_nums, fib_nums[i-2]+fib_nums[i-1])
    }
    for _, num := range fib_nums {
        if IsPrime(num) {
            return num
        }
    }
    return -1
}

func IsPrime(num int) bool {
    if num <= 1 {
        return false
    }
    for i := 2; i < int(math.Sqrt(float64(num))); i++ {
        if num % i == 0 {
            return false
        }
    }
    return true
}



