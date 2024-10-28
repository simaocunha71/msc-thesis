    result := make([]string,0)
    for _,v := range arr {
        if v >= 1 && v <=9 {
            result = append(result,name[v])
        }
    }
    sort.Strings(result)
    sort.Slice(result,func(i,j int)bool {
        return result[i] > result[j]
    })
    return result
}



