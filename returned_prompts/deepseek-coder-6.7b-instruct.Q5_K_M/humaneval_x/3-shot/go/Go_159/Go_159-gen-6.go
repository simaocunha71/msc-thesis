    Eaten := need
    if remaining < need {
        Eaten = remaining
    }
    return []int{number + Eaten, remaining - Eaten}
}



