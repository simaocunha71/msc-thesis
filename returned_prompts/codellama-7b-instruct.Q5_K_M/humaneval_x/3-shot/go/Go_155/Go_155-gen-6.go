    count := make(map[bool]int)
    for _, digit := range strconv.Itoa(num) {
        digit_int, _ := strconv.Atoi(string(digit))
        if digit_int%2 == 0 {
            count[true] += 1
        } else {
            count[false] += 1
        }
    }
    return [2]int{count[true], count[false]}
}



