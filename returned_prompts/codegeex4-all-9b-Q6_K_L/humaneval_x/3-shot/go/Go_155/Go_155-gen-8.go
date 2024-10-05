    num_str := strconv.Itoa(num)
    num_str = num_str[1:] // remove the negative sign
    even_count := 0
    odd_count := 0

    for _, c := range num_str {
        if c == '0' || c == '2' || c == '4' || c == '6' || c == '8' {
            even_count += 1
        } else {
            odd_count += 1
        }
    }

    return [2]int{even_count, odd_count}
}


