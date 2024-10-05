    even, odd := 0, 0
    digits := strconv.Itoa(num)
    for _, digit := range digits {
        if digit%2 == 0 {
            even++
        } else {
            odd++
        }
    }
    return [2]int{even, odd}
}



