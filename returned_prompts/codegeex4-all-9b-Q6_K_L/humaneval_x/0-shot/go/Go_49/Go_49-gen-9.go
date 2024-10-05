func Modp(n int, p int) int {
    var m int
    for i := n; i > 0; i /= 2 {
        if i%2 == 1 {
            m = (m * 2) % p
        }
        i /= 2
        m = (m * m) % p
    }
    return m
}