
    // Convert x to string
    str := strconv.Itoa(x)

    // Reverse the string
    str = reverse(str)

    // Check if shift is greater than length of the string
    if len(str) < shift {
        shift = shift % len(str)
    }

    // Check if shift is 0
    if shift == 0 {
        return str
    }

    //