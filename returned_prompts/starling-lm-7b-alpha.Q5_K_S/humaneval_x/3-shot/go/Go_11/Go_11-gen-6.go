    result := make([]byte, 0)

    for _, c := range a {
        result = append(result, byte(c^byte(b[len(b)-len(a):])))
    }
    return string(result)
}



