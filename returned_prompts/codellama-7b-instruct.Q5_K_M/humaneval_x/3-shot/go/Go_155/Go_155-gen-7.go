    even_count := 0
    odd_count := 0
    for num > 0 {
        if num % 2 == 0 {
            even_count += 1
        }else {
            odd_count += 1
        }
        num /= 10
    }
    return [2]int{even_count, odd_count}
}



