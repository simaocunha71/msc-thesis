    floatValue, _ := strconv.ParseFloat(value, 64)
    if floatValue > 0 {
        return int(floatValue + math.Copysign(0.5, floatValue))
    } else {
        return int(floatValue - math.Copysign(0.5, floatValue))
    }
}



