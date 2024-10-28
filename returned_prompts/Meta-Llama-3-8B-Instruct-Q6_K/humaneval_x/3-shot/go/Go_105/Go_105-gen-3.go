    names := [...]string{"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
    var result []string
    for _, v := range arr {
        if v >= 1 && v <= 9 {
            result = append(result, names[int(v)])
        }
    }
    sort.Slice(result, func(i, j int) bool {
        return len(result[i]) > len(result[j])
    })
    for i, j := 0, len(result)-1; i < j; i, j = i+1, j-1 {
        result[i], result[j] = result[j], result[i]
    }
    return result
}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}  //  return result}