    floatValue, _ := strconv.ParseFloat(value, 64)
    return int(math.Copysign(math.Floor(math.Abs(floatValue) + 0.5), floatValue))
}



