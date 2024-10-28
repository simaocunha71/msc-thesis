func Modp(n, p int) int {
    m := 1
    for n > 0 {
        if n&1 == 1 {
            m = (m * 2) % p
        }
        n = n >> 1
        p = (p * p) % p
    }
    return m
}

func main() {
    fmt.Println(Modp(3, 5))
    fmt.Println(Modp(1101, 101))
    fmt.Println(Modp(0, 101))
    fmt.Println(Modp(3, 11))
    fmt.Println(Modp(100, 101))
}