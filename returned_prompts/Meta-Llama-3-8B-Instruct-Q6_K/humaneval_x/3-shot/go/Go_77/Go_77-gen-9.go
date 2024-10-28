    c := int(math.Ceil(math.Pow(float64(a), 1/3)))
    return c*c*c == a
}
// or
func Iscube(a int) bool {
    c := int(math.Ceil(math.Pow(float64(a), 1/3)))
    return c * c * c == a
}