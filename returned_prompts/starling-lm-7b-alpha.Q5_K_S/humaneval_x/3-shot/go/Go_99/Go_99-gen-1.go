    float_value, _ := strconv.ParseFloat(value, 64)
    int_value := math.Round(float_value)
    if float_value-int_value > 0.5 {
        int_value += 1
    }

    return int(int_value)
}



