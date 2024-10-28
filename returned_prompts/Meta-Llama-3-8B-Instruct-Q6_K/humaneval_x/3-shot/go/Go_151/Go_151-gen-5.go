    sum := 0
    for _, num := range lst {
        if num > 0 && int(num) == num {
            sum += int(num) * int(num)
        }
    }
    return sum
}