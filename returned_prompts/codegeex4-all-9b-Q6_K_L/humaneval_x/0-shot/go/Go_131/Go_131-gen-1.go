func Digits(n int) int {
    if n == 0 {
        return 0
    }
    product := 1
    for n > 0 {
        digit := n % 10
        if digit%2 == 1 {
            product *= digit
        }
        n = n / 10
    }
    return product
}

func main() {
    fmt.Println(Digits(1))    // 1
    fmt.Println(Digits(4))    // 0
    fmt.Println(Digits(235))  // 15
}
