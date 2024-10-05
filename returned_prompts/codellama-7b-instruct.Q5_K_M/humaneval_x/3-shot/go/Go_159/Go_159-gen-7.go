    if number + remaining < need {
        return []int{number + remaining, 0}
    } else {
        return []int{need, number + remaining - need}
    }
}



