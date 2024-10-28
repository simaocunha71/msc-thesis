    for _, value := range lst {
        if value < 0 || !math.IsInteger(value) {
            continue A
        }
        value = value * value
    }

    return 0
}
