    max_score := math.Inf(-1)
    max_extension := ""
    for _, ext := range extensions {
        score := float64(math.CountUpperCase(ext)) - float64(math.CountLowerCase(ext))
        if score == max_score {
            if ext < max_extension {
                max_extension = ext
            }
        } else if score > max_score {
            max_extension = ext
            max_score = score
        }
    }
    return class_name + "." + max_extension
}



