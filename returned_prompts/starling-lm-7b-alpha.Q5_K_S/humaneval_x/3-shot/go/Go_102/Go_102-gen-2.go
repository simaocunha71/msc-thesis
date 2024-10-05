    if x%2 == 0 {
        if x == y {
            return x
        }
        if x + 1 == y {
            return x + 1
        }
    }
    if y%2 == 0 {
        if x == y {
            return y
        }
        if y - 1 == x {
            return y - 1
        }
    }
    return -1
}



