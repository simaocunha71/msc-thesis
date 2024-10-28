    count := 0
    for _, num := range nums {
        if num > 10 {
            str := strconv.Itoa(num)
            if len(str) > 1 && (str[0]%2 != 0 && str[len(str)-1]%2 != 0) {
                count++
            }
        }
    }
    return count
}