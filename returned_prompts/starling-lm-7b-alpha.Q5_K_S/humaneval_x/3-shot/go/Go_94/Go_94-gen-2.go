    max := 0
    for _, v := range lst {
        if v > max {
            max = v
        }
    }
    maxStr := strconv.Itoa(max)
    sum := 0
    for _, c := range maxStr {
        sum += int(c - '0')
    }
    return sum
}



