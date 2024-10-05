    length := len(text)
    if length <= 1 {
        return true
    }

    left := 0
    right := length - 1
    for right > left {
        if text[left] != text[right] {
            return false
        }
        left += 1
        right -= 1
    }
    return true
}



