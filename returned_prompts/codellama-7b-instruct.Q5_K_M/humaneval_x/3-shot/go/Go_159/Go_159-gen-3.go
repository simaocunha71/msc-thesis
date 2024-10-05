    if number + remaining >= need {
        return []int{number + remaining - need, need}
    }else {
        return []int{number + remaining, 0}
    }
}



