func CountNums(arr []int) int {
    count := 0
    for _, num := range arr {
        sum := 0
        absNum := int(math.Abs(float64(num)))
        for absNum > 0 {
            digit := absNum % 10
            absNum /= 10
            sum += digit
        }
        if sum > 0 {
            count++
        }
    }
    return count
}