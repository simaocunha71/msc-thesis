    result := make([]int, 0)
    for i := 0; i < len(l); i++ {
        if i % 3 == 0 {
            temp := make([]int, 0)
            for _, val := range l {
                if i % 3 == 0 && val != l[i] {
                    temp = append(temp, val)
                }
            }
            sort.Ints(temp)
            result = append(result, temp...)
        } else {
            result = append(result, l[i])
        }
    }
    return result
}  // or, more concisely:
func SortThird(l []int) []int {
    result := make([]int, 0)
    for i, v := range l {
        if i%3 == 0 {
            temp := make([]int, 0)
            for _, val := range l {
                if i%3 == 0 && val != v {
                    temp = append(temp, val)
                }
            }
            sort.Ints(temp)
            result = append(result, temp...)
        } else {
            result = append(result, v)
        }
    }
    return result
}  // or, even more concisely:
func SortThird(l []int) []int {
    result := make([]int, 0)
    for _, v := range l {
        if i := len(result); i%3 == 0 {
            temp := make([]int, 0)
            for _, val := range l {
                if i%3 == 0 && val != v {
                    temp = append(temp, val)
                }
            }
            sort.Ints(temp)
            result = append(result, temp...)
        } else {
            result = append(result, v)
        }
    }
    return result
}  // or, using a slice of slices:
func SortThird(l []int) []int {
    result := [][]int{{}, {}, {}}
    for _, v := range l {
        if i := len(result[0]); i%3 == 0 {
            temp := make([]int, 0)
            for _, val := range l {
                if i%3 == 0 && val != v {
                    temp = append(temp, val)
                }
            }
            sort.Ints(temp)
            result[0] = temp
        } else {
            result[i%3] = append(result[i%3], v)
        }
    }
    var res []int
