    even_count := 0
    odd_count := 0
    str_num := strconv.Itoa(num)

    for _, char := range str_num {
        if char < '0' || char > '9' {
            continue
        }
        digit := int(char - '0')
        if digit % 2 == 0 {
            even_count++
        } else {
            odd_count++
        }
    }
    return [2]int{even_count, odd_count}
}



