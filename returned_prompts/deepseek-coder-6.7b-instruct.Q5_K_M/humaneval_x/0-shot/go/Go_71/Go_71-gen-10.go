    if (a + b <= c) || (a + c <= b) || (b + c <= a) {
        return -1
    }

B:
    s := (a + b + c) / 2
    area := math.Sqrt(s * (s - a) *