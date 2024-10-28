    count := 0
    for _, num := range arr {
        if sumDigits(num) > 0 {
            count++
        }
    }
    return count
}

func sumDigits(n int) int {
    sum := 0
    for n != 0 {
        digit := n % 10
        sum += digit
        n = n / 10
    }
    return sum
}



