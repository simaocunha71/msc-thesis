func Modp(n, p int) int {
    res := 1
    for n > 0 {
        if n%2 == 1 {
            res = (res * p) % n
        }
        p = (p * p) % n
        n = n / 2
    }
    return res
}