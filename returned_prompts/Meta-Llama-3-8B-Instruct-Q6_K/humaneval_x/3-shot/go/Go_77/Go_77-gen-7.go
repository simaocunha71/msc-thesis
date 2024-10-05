    c := int(math.Ceil(math.Pow(float64(int(math.Abs(float64(a)))), (1.0/3.0))))
    return c*c*c == math.Abs(float64(a))
}