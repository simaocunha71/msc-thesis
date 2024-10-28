    count := 0
    for _, num := range nums {
        str := strconv.Itoa(num)
        first_digit := int(str[0] - '0')
        last_digit := int(str[len(str)-1] - '0')
        if num > 10 && (first_digit%2 == 1) && (last_digit%2 == 1) {
            count++
        }
    }
    return count
}