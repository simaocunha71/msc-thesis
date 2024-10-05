    float_value, _ := strconv.ParseFloat(value, 64)
    rounded_value := math.Round(float_value)
    int_value := int(rounded_value)
    if math.Abs(float_value - float64(int_value)) == 0.5 && rounded_value > 0 {
        return int_value + 1
    }
    return int_value
}



