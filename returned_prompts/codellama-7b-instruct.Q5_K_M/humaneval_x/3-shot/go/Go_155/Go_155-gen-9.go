    even_count := 0
    odd_count := 0

    for _, digit := range strconv.Itoa(num) {
        digit_val, _ := strconv.Atoi(string(digit))
        if digit_val % 2 == 0 {
            even_count += 1
        } else {
            odd_count += 1
        }
    }

    return [2]int{even_count, odd_count}
}



