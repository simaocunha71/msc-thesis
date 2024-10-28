func Iscube(a int) bool {
    return a > 0 && math.Pow(math.Floor(math.Pow(float64(a), 1/3.)), 3) == float64(a)
}