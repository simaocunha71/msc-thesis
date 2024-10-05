    var max int = l[0]
    for _, value := range l {
        if value > max {
            max = value
        }
    }
    return max
}  // O(n) time complexity



