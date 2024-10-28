    count := 0
    for _, num := range arr {
        if num < 0 {
            num = -num
        }
        sum := 0
        for num > 0 {
            digit := num % 10
            sum += digit
            num /= 10
        }
        if sum > 0 {
            count++
        }
    }
    return count
}

// Alternative solution using strconv.Atoi and math.Abs
func CountNums(arr []int) int {
    count := 0
    for _, num := range arr {
        if num < 0 {
            num = -num
        }
        if math.Abs(float64(strconv.Atoi(strconv.Itoa(int(num))))) > 0 {
            count++
        }
    }
    return count
}