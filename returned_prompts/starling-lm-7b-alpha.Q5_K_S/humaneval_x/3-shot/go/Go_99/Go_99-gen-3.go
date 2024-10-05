    num, _ := strconv.ParseFloat(value, 64)
    if math.Floor(num) == num {
        return int(num)
    }
    if num > 0 {
        return int(math.Ceil(num))
    }
    return int(math.Floor(num))
}



