    sum := 0
    for i, num := range arr[:k] {
        s := strconv.Itoa(num)
        if len(s) <= 2 {
            sum += num
        }
    }
    return sum
}