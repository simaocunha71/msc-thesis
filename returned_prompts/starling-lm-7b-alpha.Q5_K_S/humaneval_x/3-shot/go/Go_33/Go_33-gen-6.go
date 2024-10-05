    thirdIndexes := make([]int,0)
    for i, v := range l {
        if i%3 == 0 {
            thirdIndexes = append(thirdIndexes, i)
        }
    }
    sort.Ints(thirdIndexes)
    result := make([]int, len(l))
    for i, v := range l {
        if i%3 == 0 {
            result[i] = l[thirdIndexes[i/3]]
        }else {
            result[i] = v
        }
    }
    return result
}



