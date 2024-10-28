    max_strength := math.MinInt
    max_index := -1
    for i, s := range extensions {
        strength := 0
        for _, c := range s {
            if c >= 'A' && c <= 'Z' {
                strength += 1
            } else if c >= 'a' && c <= 'z' {
                strength -= 1
            }
        }
        if strength > max_strength {
            max_strength = strength
            max_index = i
        }
    }
    return class_name + "." + extensions[max_index]
}

