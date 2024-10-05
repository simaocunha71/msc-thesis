    even, odd := 0, 0
    for _, digit := range strconv.Itoa(num) {
        if digit%2 == 0 {
            even++
        } else {
            odd++
        }
    }
    return [2]int{even, odd}
}



