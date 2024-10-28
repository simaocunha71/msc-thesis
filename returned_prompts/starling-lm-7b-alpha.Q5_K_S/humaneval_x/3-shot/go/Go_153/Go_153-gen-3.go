    result := ""
    max_strength := -1
    for _, ext := range extensions {
        strength := math.Floor(math.Abs(float64(len(ext[:0]))-len(ext[1:])))*-1
        if strength > max_strength {
            max_strength = strength
            result = class_name + "." + ext
        }
    }
    return result
}



