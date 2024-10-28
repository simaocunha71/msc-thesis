    result := ""
    current_strength := -math.MaxInt32

    for _, ext := range extensions {
        strength := math.Max(float64(len(ext)-strings.Count(ext, string(byte('a'))))-math.Floor(float64(len(ext)-strings.Count(ext, string(byte('A'))))), 0)
        if strength > current_strength {
            current_strength = strength
            result = ext
        }
    }
    return class_name + "." + result
}



