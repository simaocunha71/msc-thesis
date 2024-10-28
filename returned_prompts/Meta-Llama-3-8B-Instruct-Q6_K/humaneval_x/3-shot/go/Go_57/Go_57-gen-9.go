    var increasing bool = true
    var decreasing bool = true
    for i := 1; i < len(l); i++ {
        if l[i] > l[i-1] {
            decreasing = false
        }else if l[i] < l[i-1] {
            increasing = false
        }
    }
    return increasing || decreasing
}