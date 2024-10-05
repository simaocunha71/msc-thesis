    strongest_ext := ""
    highest_strength := -math.MaxFloat64

    for _, ext := range extensions {
        CAP, SM := 0, 0
        for _, c := range ext {
            if 'A' <= c && c <= 'Z' {
                CAP++
            } else if 'a' <= c && c <= 'z' {
                SM++
            }
        }
        strength := float64(CAP) - float64(SM)
        if strength > highest_strength {
            highest_strength = strength
            strongest_ext = ext
        }
    }

    return class_name + "." + strongest_ext
}



