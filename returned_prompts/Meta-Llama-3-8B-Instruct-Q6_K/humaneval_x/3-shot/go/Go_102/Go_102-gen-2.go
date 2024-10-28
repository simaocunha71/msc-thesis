    if x%2 == 0 {
        return y
    } else if y%2 == 0 {
        return y - 1
    } else if x <= y {
        return -1
    } else {
        return x - 1
    }
}