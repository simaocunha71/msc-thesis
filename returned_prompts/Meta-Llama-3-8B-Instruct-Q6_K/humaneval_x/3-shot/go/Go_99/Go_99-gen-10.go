    num, _ := strconv.ParseFloat(value, 64)
    intNum := math.Round(num)
    if math.Abs(float64(int(intNum))) < math.Abs(float64(int(intNum)+1)) {
        return int(intNum)
    } else {
        return int(intNum + 1)
    }
}