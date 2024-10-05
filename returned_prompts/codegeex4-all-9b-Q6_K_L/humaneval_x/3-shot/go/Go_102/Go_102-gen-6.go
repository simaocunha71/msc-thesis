    if y < x {
        return -1
    }else if x % 2 == 0 {
        return x
    }else if y % 2 == 0 {
        return y
    }else {
        return y - 1
    }
}

