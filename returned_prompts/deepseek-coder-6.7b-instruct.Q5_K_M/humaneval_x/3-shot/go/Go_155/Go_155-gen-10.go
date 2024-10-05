    even_count := 0
    odd_count := 0
    num_string := strconv.Itoa(num)

    for _, v := range num_string {
        if v := int(v - '0'); v % 2 == 0 {
            even_count++
        } else {
            odd_count++
        }
    }
    return [2]int{even_count, odd_count}
}



