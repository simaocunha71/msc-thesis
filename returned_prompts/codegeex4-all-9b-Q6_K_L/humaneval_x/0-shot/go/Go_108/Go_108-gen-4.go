func CountNums(arr []int) int {
    count := 0
    for _, num := range arr {
        if sumDigits(num) > 0 {
            count++
        }
    }
    return count
}

func sumDigits(num int) int {
    sum := 0
    for _, digit := range strconv.Itoa(abs(num)) {
        d, _ := strconv.Atoi(string(digit))
        sum += d
    }
    return sum
}

func abs(num int) int {
    if num < 0 {
        return -num
    }
    return num
}