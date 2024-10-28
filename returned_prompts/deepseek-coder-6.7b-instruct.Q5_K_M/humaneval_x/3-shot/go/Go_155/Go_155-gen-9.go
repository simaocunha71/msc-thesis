    even_count := 0
    odd_count  := 0

    str_num := strconv.Itoa(num)
    if str_num[0] == '-' {
        str_num = str_num[1:]
    }

    for _, v := range str_num {
        digit, _ := strconv.Atoi(string(v))
        if digit % 2 == 0 {
            even_count++
        } else {
            odd_count++
        }
    }

    return [2]int{even_count, odd_count}
}



