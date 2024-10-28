    if n == 1 {
        return 2
    }
    if n == 2 {
        return 3
    }
    if n == 3 {
        return 5
    }
    if n == 4 {
        return 13
    }
    if n == 5 {
        return 89
    }

    fibs := []int{1, 1, 2, 3, 5, 13, 21, 34, 55, 89}
    fibs_length := len(fibs)
    fibs_index := n - 5
    fibs = append(fibs, 0)
    for i := fibs_length; i <= fibs_index; i++ {
        fibs[i] = fibs[i-1] + fibs[i-2]
    }
    num := fibs[fibs_index]
    for !is_prime(num) {
        num = num + 1
    }
    return num
}

func is_prime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

