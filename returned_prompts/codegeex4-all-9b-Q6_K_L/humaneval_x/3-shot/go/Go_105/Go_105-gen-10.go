    m := make(map[int]int)
    for _, num := range arr {
        m[num] = m[num] + 1
    }

    for i := 1; i <= len(arr); i++ {
        if m[i] == 0 {
            return i
        }
    }

    return -1
}

// Given a list