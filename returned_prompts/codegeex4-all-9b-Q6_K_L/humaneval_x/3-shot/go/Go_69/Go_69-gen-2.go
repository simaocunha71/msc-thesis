    var result int = -1
    var count int = 0
    var max int = 0

    for _, num := range lst {
        count = 0
        for _, num2 := range lst {
            if num == num2 {
                count += 1
            }
        }
        if count >= num && num > max {
            result = num
            max = num
        }
    }
    return result
}

