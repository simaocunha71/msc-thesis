    result := ""
    for x > 0 {
        x, remainder := x/ int(math.Pow(float64(base), float64(int(math.Ceil(math.Log(float64(x))))))),
        remainder % int(base)
        result = strconv.Itoa(remainder) + result
    }
    return result
}
