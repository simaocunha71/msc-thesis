    if n % 2 == 1 {
        return false
    }

    for i := 2; i <= n / 2; i += 2{
        if n == i + i + i + i{
            return true
        }
    }
    return false
}



