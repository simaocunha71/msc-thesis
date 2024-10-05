func Iscube(a int) bool {
    root := math.Pow(math.Abs(float64(a)), 1/3)
    return math.Abs(root-math.Floor(root)) < 0.00001
}
