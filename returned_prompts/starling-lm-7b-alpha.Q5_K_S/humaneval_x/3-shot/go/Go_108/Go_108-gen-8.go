    result := 0
    for _, v := range arr {
        if SumOfDigits(v) > 0 {
            result += 1
        }
    }
    return result
}

func SumOfDigits(n int) int {
    sum := 0
    for n != 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}



