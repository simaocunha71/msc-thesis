    result := 0
    for n > 0 {
        if n % 10 % 2 == 1{
            result += n % 10
        }
        n /= 10
    }
    return result
}



