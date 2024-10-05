    if remaining <= need - number{
        return []int{number + remaining, 0}
    }
    return []int{need, number + remaining - need}
}



