    if len(strings) == 0 {
        return nil
    }

    result := strings[0]
    for _, s := range strings[1:] {
        if len(result) < len(s) {
            result = s
        }
    }
    return result
}



