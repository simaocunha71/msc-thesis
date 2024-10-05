    count := 0
    for _, num := range arr {
        if num < 0 {
            num = -num
        }
        sum := 0
        str := strconv.Itoa(int(num))
        for _, c := range str {
            sum += int(c - '0')
        }
        if sum > 0 {
            count++
        }
    }
    return count
}
