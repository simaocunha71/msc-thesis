    if n%2 == 0 {
        return y
    }
    i := 3
    for {
        if n%i == 0 {
            return x
        }
        if i*i > n {
            return y
        }
        i += 2
    }
}



