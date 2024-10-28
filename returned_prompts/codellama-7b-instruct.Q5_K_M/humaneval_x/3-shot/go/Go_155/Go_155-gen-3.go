    even_count := 0
    odd_count := 0

    for _, digit := range strconv.Itoa(num) {
        if digit == '0' {
            even_count += 1
        } else if digit == '1' {
            odd_count += 1
        }
    }
    return [2]int{even_count, odd_count}
}



