    even := 0
    odd := 0

    for ; num > 0; num /= 10 {
        if num % 10 % 2 == 0 {
            even++
        } else {
            odd++
        }
    }
    return [2]int{even, odd}
}



