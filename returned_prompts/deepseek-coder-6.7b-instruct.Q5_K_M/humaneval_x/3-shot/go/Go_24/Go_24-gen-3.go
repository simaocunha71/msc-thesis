    for i := n - 1; i > 0; i-- {
        if n%i == 0 {
            return i
        }
    }
    return -1 // This is just to avoid compiler error
}



