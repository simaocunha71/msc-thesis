    even_count := 0
    odd_count := 0
    for {
        digit := num % 10
        if digit % 2 == 0 {
            even_count += 1
        }else{
            odd_count += 1
        }
        if digit == 0 {
            break
        }
        num /= 10
    }
    return [2]int{even_count, odd_count}
}



