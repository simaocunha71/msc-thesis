    if remaining-number<need {
        return []int{need+number, 0}
    }else {
        return []int{number + need, remaining - need}
    }
}



