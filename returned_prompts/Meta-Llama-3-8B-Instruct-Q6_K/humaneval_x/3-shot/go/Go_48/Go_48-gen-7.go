    text = strings.ToLower(text)
    left, right := 0, len(text) - 1
    for left < right {
        if text[left] != text[right] {
            return false
        }
        left++
        right--
    }
    return true
}