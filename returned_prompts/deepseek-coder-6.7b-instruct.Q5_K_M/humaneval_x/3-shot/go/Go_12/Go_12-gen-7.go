    if len(strings) == 0 {
        return nil
    }

    longest := strings[0]
    for _, str := range strings {
        if len(str) > len(longest) {
            longest = str
        }
    }

    return longest
}



