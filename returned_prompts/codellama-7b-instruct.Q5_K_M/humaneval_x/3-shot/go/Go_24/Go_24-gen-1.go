    if n == 1 {
        return 1
    }
    for i := n; i > 1; i--{
        if n % i == 0 {
            return i
        }
    }
    return 1
}



