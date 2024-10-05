    count := 0
    for _, num := range nums {
        if num > 10 {
            str := strconv.Itoa(num)
            first_digit := int(str[0] - '0')
            last_digit := int(str[len(str)-1] - '0')
            if (first_digit % 2 != 0) && (last_digit % 2 != 0) {
                count++
            }
        }
    }
    return count
}