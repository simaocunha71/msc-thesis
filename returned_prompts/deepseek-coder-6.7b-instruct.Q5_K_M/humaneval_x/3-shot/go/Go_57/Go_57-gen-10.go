    if len(l) < 2 {
        return true
    }

    var direction int
    for i := 1; i < len(l); i++ {
        switch {
        case l[i-1] < l[i]:
            if direction != 0 && direction != 1 {
                return false
            }
            direction = 1
        case l[i-1] > l[i]:
            if direction != 0 && direction != -1 {
                return false
            }
            direction = -1
        }
    }

    return true
}



