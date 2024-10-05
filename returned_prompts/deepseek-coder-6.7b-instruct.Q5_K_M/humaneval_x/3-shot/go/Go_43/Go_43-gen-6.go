    seen := make(map[int]bool)

    for _, num := range l {
        if seen[-num] {
            return true
        }
        seen[num] = true
    }

    return false
}



