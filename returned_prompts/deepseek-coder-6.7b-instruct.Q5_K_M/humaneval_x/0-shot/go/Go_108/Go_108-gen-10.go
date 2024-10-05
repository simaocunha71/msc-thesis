    count := 0

    for _, value := range arr {
        if value < 0 {
            str := strconv.Itoa(value)
            sum := 0
            for _, digit := range str[1:] {
                digitInt, _ := strconv.Atoi(string(digit))
                sum += digitInt
            }
            if sum > 0 {
                count++
            }
        } else {
            str := strconv.Itoa(value)
            sum := 0
            for _, digit := range str {
                digitInt, _ := strconv.Atoi(string(digit))
                sum += digitInt
            }
            if sum > 0 {
                count++
            }
        }
    }

    return count
}

This is a Python solution:

