func CountNums(arr []int) int {
    var count int = 0
    for _, num := range arr {
        if sumDigits(num) > 0 {
            count++
        }
    }
    return count
}

func sumDigits(n int) int {
    var sum int = 0
    abs := int(math.Abs(float64(n)))
    for abs > 0 {
        sum += abs % 10
        abs /= 10
    }
    return sum
}