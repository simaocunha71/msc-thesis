    for _, v := range arr[0:k] {
        if len(strconv.Itoa(v)) > 2 {
            continue A
        }
    }
    var sum int
    for _, v := range arr[0:k] {
        sum += v
    }
    return sum
}
