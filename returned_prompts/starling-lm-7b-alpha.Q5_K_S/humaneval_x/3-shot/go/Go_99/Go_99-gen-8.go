    num, _ := strconv.ParseFloat(value, 64)
    if math.Trunc(num) == num {
        return int(num)
    }
    if num > 0 {
        return int(math.Ceil(num))
    }
    return int(math.Floor(num))
}



