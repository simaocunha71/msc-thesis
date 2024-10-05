    l = removeDuplicates(l)
    sort.Ints(l)
    return l
}

func removeDuplicates(l []int) []int {
    l2 := make([]int, len(l))
    j := 0
    for _, v := range l {
        if j >= len(l2) || l2[j] != v {
            l2[j] = v
            j++
        }
    }
    return l2[:j]
}



