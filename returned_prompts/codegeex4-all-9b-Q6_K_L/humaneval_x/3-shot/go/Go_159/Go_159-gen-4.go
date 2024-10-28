    if remaining >= need{
        return []int{number+need, remaining-need}
    }else{
        return []int{number+remaining, 0}
    }
}

