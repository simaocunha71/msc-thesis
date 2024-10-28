for _, r := range s {
    switch {
    case strings.ContainsRune("aeiouy", r):
        // If we find a vowel, we should break out of the loop because
        // there can only be one.
        break A
    }
}

return 0
}
