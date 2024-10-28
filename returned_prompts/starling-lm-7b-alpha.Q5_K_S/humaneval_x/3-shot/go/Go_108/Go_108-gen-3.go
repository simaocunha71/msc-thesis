    result := 0
    for _, i := range arr {
        if SumOfDigits(i) > 0 {
            result++
        }
    }
    return result
}

func SumOfDigits(n int) int {
    n = math.Abs(n)
    sum := 0
    for n > 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}



