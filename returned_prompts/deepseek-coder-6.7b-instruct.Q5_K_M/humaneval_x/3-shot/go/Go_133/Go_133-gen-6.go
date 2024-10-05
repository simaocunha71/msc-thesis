    var result int = 0

    for  _, num := range lst {
        ceilNum := int(math.Ceil(num))
        result += ceilNum * ceilNum
    }

    return result
}



