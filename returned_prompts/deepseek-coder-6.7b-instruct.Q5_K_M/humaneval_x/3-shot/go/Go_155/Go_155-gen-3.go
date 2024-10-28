    even_count := 0
    odd_count := 0
    num_str := strconv.Itoa(num)

    for _, c := range num_str {
        digit, _ := strconv.Atoi(string(c))
        if digit % 2 == 0 {
            even_count++
        } else {
            odd_count++
        }
    }
    return [2]int{even_count, odd_count}
}



