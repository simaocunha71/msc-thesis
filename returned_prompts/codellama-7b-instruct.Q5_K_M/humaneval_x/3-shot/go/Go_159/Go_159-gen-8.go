    if remaining < need {
        return []int{number + remaining, 0}
    } else {
        return []int{number + need, remaining - need}
    }
}



