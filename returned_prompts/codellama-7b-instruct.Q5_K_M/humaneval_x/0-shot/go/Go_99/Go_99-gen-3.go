    // TODO - your code here
    // 2019-09-19 16:27:04.127641142 +0800 CST m=+0.094729445
    f, err := strconv.ParseFloat(value, 64)
    if err != nil {
        return 0
    }

    c := math.Ceil(f)
    d := math.Floor(f)
    if f == c {
        return int(c)
    }
    if f == d {
        return int(d)
    }

    if c - f < f - d {
        return int(c)
    }
    return int(d)
}



// 2019-09-19 16:28:04.128641921 +0800 CST m=+0.094809446
func ClosestInteger(value string) int {
    f, err := strconv.ParseFloat(value, 64)
    if err != nil {
        return 0
    }
    c := math.Ceil(f)
    d := math.Floor(f)
    if c - f < f - d {
        return int(c)
    }
    return int(d)
}



// 2019-09-19 16:29:04.129641922 +0800 CST m=+0.094889447
func ClosestInteger(value string) int {
    f, err := strconv.ParseFloat(value, 64)
    if err != nil {
        return 0
    }
    c := math.Ceil(f)
    d := math.Floor(f)
    if c == d {
        return int(c)
    }
    if c - f < f - d {
        return int(c)
    }
    return int(d)
}



// 2