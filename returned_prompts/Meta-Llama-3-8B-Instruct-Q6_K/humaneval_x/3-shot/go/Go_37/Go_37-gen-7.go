    result := make([]int, 0, len(l))
    for i, v := range l {
        if i % 2 == 0 {
            result = append(result, sort.IntsAreSorted([]int{v}) )
        } else {
            result = append(result, v)
        }
    }
    return result
}
}
}
}}


