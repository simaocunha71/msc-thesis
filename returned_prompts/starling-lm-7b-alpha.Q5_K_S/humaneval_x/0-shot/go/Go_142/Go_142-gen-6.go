    result := 0
    for i := 0; i < len(lst); i++ {
        if i%3 == 0 {
            result += lst[i] * lst[i]
        } else if i%4 == 0 && i%3 != 0 {
            result += lst[i] * lst[i] * lst[i]
        }
    }
    return result
}






func SumSquares(lst []int) int {
    result := 0
    for i, v := range lst {
        if i%3 == 0 {
            result += v * v
        } else if i%4 == 0 && i%3 != 0 {
            result += v * v * v
        }
    }
    return result
}






func SumSquares(lst []int) int {
    result := 0
    for _, v := range lst {
        if i := index(v, lst); i%3 == 0 {
            result += v * v
        } else if i%4 == 0 && i%3 != 0 {
            result += v * v * v
        }
    }
    return result
}






func SumSquares(lst []int) int {
    result := 0
    for i, v := range lst {
        if i%3 == 0 {
            result += v * v
        } else if i%4 == 0 && i%3 != 0 {
            result += v * v * v
        }
    }
    return result
}






func SumSquares(lst []int) int {
    result := 0
    for i, v := range lst {
        if i%3 == 0 {
            result += v * v
        } else if i%4 == 0 && i%3 != 0 {
            result += v * v * v
        }
    }
    return result
}





func SumSquares(lst []int) int {
    result := 0
    for _, v := range lst