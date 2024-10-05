    result := make([]int,0)
    for _, i := range x{
        str := strconv.Itoa(i)
        if !strings.Contains(str,"2") && !strings.Contains(str,"4") && !strings.Contains(str,"6") && !strings.Contains(str,"8"){
            result = append(result,i)
        }
    }
    sort.Ints(result)
    return result
}



