    vowels := strings.Split(s, "")
    count := 0
    for _, vowel := range vowels {
        switch vowel {
        case "a", "e", "i", "o", "u", "y":
            count += 1
        }
    }
    return count
}



