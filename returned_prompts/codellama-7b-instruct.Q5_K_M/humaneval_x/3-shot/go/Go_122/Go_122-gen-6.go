    sum := 0
    for i, x := range arr[:k] {
        if i == 0 {
            sum = x
        } else {
            sum += x
        }
    }
    return sum
}



