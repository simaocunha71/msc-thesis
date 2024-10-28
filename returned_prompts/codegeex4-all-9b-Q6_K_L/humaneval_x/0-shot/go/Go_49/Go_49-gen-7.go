func Modp(n, p int) int {
    res := 1
    for i := n; i > 0; i /= 2 {
        if i%2 == 1 {
            res = (res * 2) % p
        }
        i /= 2
        p = (p * p) % p
    }
    return res
}