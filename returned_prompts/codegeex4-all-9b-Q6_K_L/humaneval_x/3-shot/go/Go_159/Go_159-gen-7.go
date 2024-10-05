    if need <= remaining {
        remaining -= need
        number += need
    } else {
        number += remaining
        remaining = 0
    }
    return []int{number, remaining}
}



