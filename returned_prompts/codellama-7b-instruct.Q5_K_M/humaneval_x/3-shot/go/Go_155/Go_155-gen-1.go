    var even, odd int
    for num > 0 {
        digit := num % 10
        if digit % 2 == 0 {
            even++
        } else {
            odd++
        }
        num /= 10
    }
    return [2]int{even, odd}
}



