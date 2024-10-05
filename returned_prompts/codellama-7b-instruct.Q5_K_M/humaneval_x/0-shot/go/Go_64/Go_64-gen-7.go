    for _, c := range s {
        switch c {
        case 'a', 'e', 'i', 'o', 'u', 'y':
            continue A
        }
    }

    return strings.Count(s, "aeiouy")
}

