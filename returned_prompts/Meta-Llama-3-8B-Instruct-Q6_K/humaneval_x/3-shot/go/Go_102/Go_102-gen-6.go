    if x > y {
        return -1
    }
    if x % 2 == 0 {
        return x
    }
    for i := x + 1; i <= y; i++ {
        if i % 2 == 0 {
            return i
        }
    }
    return -1
}