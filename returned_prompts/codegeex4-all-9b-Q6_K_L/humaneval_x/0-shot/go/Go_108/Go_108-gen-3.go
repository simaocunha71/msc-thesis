func CountNums(arr []int) int {
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
    absN := int(math.Abs(float64(n)))
    for absN > 0 {
        sum += absN % 10
        absN /= 10
    }
    return sum
}

func main() {
    fmt.Println(CountNums([])) // 0
    fmt.Println(CountNums([]{-1, 11, -11})) // 1
    fmt.Println(CountNums([]{1, 1, 2})) // 3
}