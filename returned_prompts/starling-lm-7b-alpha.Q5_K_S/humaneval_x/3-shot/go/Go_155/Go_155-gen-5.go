    even_count := 0
    odd_count := 0
    string_num := strconv.Itoa(num)
    for _, c := range string_num {
        if _, err := strconv.Atoi(string(c)); err != nil {
            if c % 2 == 0 {
                even_count += 1
            }else {
                odd_count += 1
            }
        }
    }
    return [2]int{even_count, odd_count}
}



