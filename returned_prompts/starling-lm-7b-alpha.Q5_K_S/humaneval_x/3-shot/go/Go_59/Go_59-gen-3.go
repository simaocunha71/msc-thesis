    i := 2
    for i <= n {
        if n % i == 0 {
            j := i
            for j <= n {
                if n % j == 0 {
                    j *= i
                }else{
                    break
                }
            }
            n /= j
        }else{
            i += 1
        }
    }
    return i - 1
}




