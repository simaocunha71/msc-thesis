func Modp(n int,p int) int {
    return int(math.Pow(float64(n),float64(p))) % p
}