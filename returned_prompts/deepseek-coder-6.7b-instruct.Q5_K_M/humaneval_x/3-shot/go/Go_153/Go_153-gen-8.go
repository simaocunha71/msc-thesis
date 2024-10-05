    var strongest_extension string
    max_strength float64 = -math.MaxFloat64

    for _, extension := range extensions {
        CAP, SM := count_upper_lower(extension)
        strength := float64(CAP) - float64(SM)
        if strength > max_strength {
            max_strength = strength
            strongest_extension = extension
        }
    }

    return class_name + "." + strongest_extension
}

func count_upper_lower(s string) (upper int, lower int) {
    for _, r := range s {
        if unicode.IsUpper(r) {
            upper++
        } else if unicode.IsLower(r) {
            lower++
        }
    }
    return
}


