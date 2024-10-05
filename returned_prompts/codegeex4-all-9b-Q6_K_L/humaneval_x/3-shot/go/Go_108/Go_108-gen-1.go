    var count int = 0
    for _, num := range arr {
        if sumDigits(num) > 0 {
            count += 1
        }
    }
    return count
}

func sumDigits(num int) int {
    var sum int
    if num < 0 {
        num = -num
        sum += -1
    }
    for num != 0 {
        sum += num % 10
        num /= 10
    }
    return sum
}

