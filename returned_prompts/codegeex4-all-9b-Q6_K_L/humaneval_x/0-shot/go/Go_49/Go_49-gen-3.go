func Modp(n int, p int) int {
    if n == 0 {
        return 1
    }
    if n % 2 == 0 {
        return Modp(n/2, p) * Modp(n/2, p) % p
    } else {
        return (Modp((n-1)/2, p) * Modp((n-1)/2, p) % p) * 3 % p
    }
}