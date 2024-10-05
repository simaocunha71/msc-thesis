    result := make([]int, 0)

    for _, i := range x {
        if strconv.Itoa(i)[0] == "1"{
            result = append(result, i)
        }
    }

    sort.Ints(result)
    return result
}



