    eat_num := need - number
    if remaining < eat_num {
        eat_num = remaining
    }
    return []int{number + eat_num, remaining - eat_num}
}