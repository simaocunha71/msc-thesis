    if number + remaining >= need{
        return []int{number + remaining - need, need - (number + remaining)}
    }else{
        return []int{number + remaining, remaining - (need - (number + remaining))}
    }
}



