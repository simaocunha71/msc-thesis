    result := 0
    for _, num := range arr {
        if SumOfDigits(num) > 0 {
            result += 1
        }
    }
    return result
}


func SumOfDigits(num int) int {
    digit_sum := 0
    for num != 0 {
        digit_sum += (num % 10)
        num /= 10
    }
    return digit_sum
}


