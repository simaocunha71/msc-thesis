    var min int
    var index int
    var found bool
    for i, v := range arr {
        if v % 2 == 0 {
            if !found || v < min {
                found = true
                min = v
                index = i
            }
        }
    }
    if found {
        return []int{min, index}
    } else {
        return []int{}
    }
} 