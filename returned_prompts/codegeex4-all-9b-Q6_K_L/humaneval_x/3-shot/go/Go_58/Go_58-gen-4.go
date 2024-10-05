    result := make([]int,0)

    for _, v := range l1 {
        if inList(l2,v) && !inList(result,v){
            result = append(result, v)
        }
    }
    return result
}

func inList(l []int,v int) bool {
    for _, i := range l {
        if i==v {
            return true
        }
    }
    return false
}



