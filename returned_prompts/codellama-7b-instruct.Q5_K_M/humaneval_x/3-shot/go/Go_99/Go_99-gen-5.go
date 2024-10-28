    number, err := strconv.ParseFloat(value, 64)

    if err != nil {
        return 0
    }

    rounded := math.Round(number)
    nearest := math.Abs(rounded - number)

    if nearest == 0.5 {
        return int(math.Copysign(1, rounded) * math.Nextafter(rounded, 2))
    }

    return int(rounded)
}



