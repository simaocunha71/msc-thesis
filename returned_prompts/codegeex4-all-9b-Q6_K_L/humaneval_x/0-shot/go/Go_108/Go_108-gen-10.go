func CountNums(arr []int) int {
    var count int

    for _, num := range arr {
        if SumDigits(num) > 0 {
            count++
        }
    }

    return count
}

func SumDigits(num int) int {
    var sum int

    for num != 0 {
        digit := num % 10
        sum += digit
        num /= 10
    }

    return sum
}

func main() {
    fmt.Println(CountNums([])) // 0
    fmt.Println(CountNums([]{-1, 11, -11})) // 1
    fmt.Println(CountNums([]{1, 1, 2})) // 3
}

