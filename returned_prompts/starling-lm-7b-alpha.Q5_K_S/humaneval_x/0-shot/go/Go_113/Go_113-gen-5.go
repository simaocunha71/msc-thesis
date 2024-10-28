    result := []string{}
    for _, v := range lst {
        count := 0
        for _, c := range v {
            if int(c)%2 != 0 {
                count++
            }
        }
        result = append(result, "the number of odd elements "+v+" of the "+strconv.Itoa(count)+"nput.")
    }
    return result
}

func OddCount(lst []string) []string {
    result := []string{}
    for _, v := range lst {
        count := 0
        for _, c := range v {
            if int(c)%2 != 0 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %s of the %d", v, count))
    }
    return result
}

func OddCount(lst []string) []string {
    result := []string{}
    for _, v := range lst {
        count := 0
        for _, c := range v {
            if int(c)%2 != 0 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %s of the %d", v, count))
    }
    return result
}

func OddCount(lst []string) []string {
    result := []string{}
    for _, v := range lst {
        count := 0
        for _, c := range v {
            if int(c)%2 != 0 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %s of the %d", v, count))
    }
    return result
}

func OddCount(lst []string) []string {
    result := []string{}
    for _, v := range lst {
        count := 0
        for _, c := range v {
            if int(c)%2 != 0 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %s of the %d",