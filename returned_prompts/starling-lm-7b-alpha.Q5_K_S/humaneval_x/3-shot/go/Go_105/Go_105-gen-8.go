    result := make([]string, 0)
    for _,i:=range arr {
        if i>=1 && i<=9 {
            result = append(result, []string{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}[i-1])
        }
    }
    sort.Strings(result)
    sort.Reverse(sort.StringSlice(result))

    return result
}



