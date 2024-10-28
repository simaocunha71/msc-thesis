    var strongest_ext string
    max_strength := math.MinInt64

    for _, ext := range extensions {
        CAP, SM := 0, 0
        for _, c := range ext {
            if 'A' <= c && c <= 'Z' {
                CAP++
            } else if 'a' <= c && c <= 'z' {
                SM++
            }
        }
        strength := CAP - SM
        if strength > max_strength {
            max_strength = strength
            strongest_ext = ext
        }
    }

    return class_name + '.' + strongest_ext
}



