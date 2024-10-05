func RightAngleTriangle(a, b, c int) bool {
    return a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a
}

func main() {
    fmt.Println(RightAngleTriangle(3, 4, 5)) // true
    fmt.Println(RightAngleTriangle(1, 2, 3)) // false
}