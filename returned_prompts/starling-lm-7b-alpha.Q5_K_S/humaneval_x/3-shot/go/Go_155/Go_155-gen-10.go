    even_count := 0
    odd_count := 0
    current := num

    for current > 0 {
        last_digit := current % 10
        if last_digit % 2 == 0 {
            even_count += 1
        }else{
            odd_count += 1
        }
        current /= 10
    }
    return [2]int{even_count, odd_count}
}



