    var count int
    for _, num := range nums {
        str := strconv.Itoa(num)
        if num > 10 && (str[0] % 2 == 1 && str[len(str) - 1] % 2 == 1) {
            count++
        }
    }
    return count
}