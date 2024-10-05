    even_count := 0
    odd_count := 0
    num_str := strconv.Itoa(num)
    num_str = num_str[1:] // ignore negative sign

    for _, digit_str := range num_str {
        digit, _ := strconv.Atoi(string(digit_str))
        if digit % 2 == 0 {
            even_count += 1
        } else {
            odd_count += 1
        }
    }
    return [2]int{even_count, odd_count}
}



