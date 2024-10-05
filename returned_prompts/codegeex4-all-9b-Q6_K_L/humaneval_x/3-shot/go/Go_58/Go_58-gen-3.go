    var result []int
    for _,i := range l1{
        for _,j := range l2{
            if i == j && !Contains(result,i){
                result = append(result,i)
            }
        }
    }
    sort.Ints(result)
    return result
}

func Contains(list []int,item int) bool{
    for _,i := range list{
        if i == item{
            return true
        }
    }
    return false
}

