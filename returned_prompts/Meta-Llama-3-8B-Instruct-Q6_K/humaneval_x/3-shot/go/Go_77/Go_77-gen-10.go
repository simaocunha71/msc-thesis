    c := int(math.Ceil(math.Pow(float64(int(math.Ceil(math.Sqrt(float64(a))))), 1/3.0)))
    return c*c*c == a
}