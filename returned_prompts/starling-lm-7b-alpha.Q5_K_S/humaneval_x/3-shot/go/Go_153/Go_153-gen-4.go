    result := class_name
    max_strength := -math.MaxInt32
    max_extension := ""

    for _, extension := range extensions {
        strength := math.Max(float64(len(extension)-math.CountUpper(extension)), math.CountLower(extension)-len(extension))
        if strength > max_strength {
            result += "." + extension
            max_strength = strength
            max_extension = extension
        }
    }

    return result
}



