    result := make([]int, 0)
    var number int = a
    if a%2 == 1 && b%2 == 0 {
        result = append(result, number)
        number += 1
    }else if a%2 == 0 && b%2 == 1 {
        result = append(result, number)
        number += 1
    }
    for {
        if number > b {
            break
        }else if number%2 == 0 {
            result = append(result, number)
        }
        number += 1
    }
    return result
}




