    if len(l) < 2 {
        return true
    }
    var increasing bool = true
    var decreasing bool = true
    for i := 0; i < len(l)-1; i++ {
        if l[i] > l[i+1] {
            decreasing = false
        } else if l[i] < l[i+1] {
            increasing = false
        }
    }
    return increasing || decreasing
}
