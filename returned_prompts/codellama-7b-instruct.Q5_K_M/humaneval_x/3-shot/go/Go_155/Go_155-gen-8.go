    even := 0
    odd := 0
    for num > 0 {
        digit := num % 10
        if digit % 2 == 0 {
            even += 1
        } else {
            odd += 1
        }
        num /= 10
    }
    return [2]int{even, odd}
}



