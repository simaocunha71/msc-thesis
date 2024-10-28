    if interval1[1] < interval2[0] || interval2[1] < interval1[0] {
        return "NO"
    }

    intersection := [2]int{math.Max(interval1[0], interval2[0]), math.Min(interval1[1], interval2[1])}

    if intersection[1] - intersection[0] == 0 || intersection[1] - intersection[0] == 1 {
        return "YES"
    }

    for i := 2; i < intersection[1]; i++ {
        if intersection[1] % i == 0 {
            return "NO"
        }
    }

    return "YES"
}

