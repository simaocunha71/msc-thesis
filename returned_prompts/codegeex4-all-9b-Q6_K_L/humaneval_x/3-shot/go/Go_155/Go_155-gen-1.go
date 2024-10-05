    even_count := 0
    odd_count := 0
    num_str := strconv.Itoa(num)
    for _, c := range num_str {
        c_int,_ := strconv.Atoi(string(c))
        if c_int % 2 == 0 {
            even_count += 1
        } else {
            odd_count += 1
        }
    }
    return [2]int{even_count, odd_count}
}