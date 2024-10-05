    count := 0
    for _, num := range nums {
        if num > 10 {
            str := strconv.Itoa(num)
            first_digit, _ := strconv.Atoi(string(str[0]))
            last_digit, _ := strconv.Atoi(string(str[len(str)-1]))
            if first_digit%2 != 0 && last_digit%2 != 0 {
                count++
            }
        }
    }
    return count
}