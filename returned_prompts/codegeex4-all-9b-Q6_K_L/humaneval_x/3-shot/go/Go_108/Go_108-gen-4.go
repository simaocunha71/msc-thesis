    count := 0
    for _, v := range arr {
        if SumDigits(v) > 0 {
            count++
        }
    }
    return count
}

func SumDigits(number int) int {
    sum := 0
    if number < 0 {
        number = -number
        sum -= 1
    }
    for number != 0 {
        sum += number % 10
        number = number / 10
    }
    return sum
}



