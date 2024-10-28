    if strings.HasSuffix(value, ".5") {
        if strings.HasPrefix(value, "-") {
            return -math.Floor(parse(value))
        } else {
            return math.Ceil(parse(value))
        }
    } else {
        return int(parse(value))
    }

}

func parse(value string) float64 {
    number, _ := strconv.ParseFloat(value, 64)
    return number
}



