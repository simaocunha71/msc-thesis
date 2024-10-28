    for _, v := range arr[0:k] {
        if v > 99 {
            continue A
        }
    }
    var sum int
    for _, v := range arr[0:k] {
        sum += v
    }
    return sum
}
