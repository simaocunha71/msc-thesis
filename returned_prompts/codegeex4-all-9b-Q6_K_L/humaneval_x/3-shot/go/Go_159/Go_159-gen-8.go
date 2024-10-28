    if remaining >= need{
        return []int{number+need,remaining-need}
    }
    return []int{number+remaining,0}
}

