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
    if num < 0 {
        num = -num
    }
    for num > 0 {
        sum += num % 10
        num /= 10
    }
    return sum
}