    sort.Slice(arr, func(i, j int) bool {
        return arr[i] < arr[j]
    })

    for i, v := range arr {
        if v >= 1 && v <= 9 {
            arr[i] = v
        } else {
            arr[i] = 0
        }
    }

    sort.Slice(arr, func(i, j int) bool {
        return arr[i] > arr[j]
    })

    res := make([]string, 0, len(arr))
    for _, v := range arr {
        if v != 0 {
            res = append(res, name(v))
        }
    }

    return res
}

func name(i int)string {
    switch i {
    case 1:
        return "One"
    case 2:
        return "Two"
    case 3:
        return "Three"
    case 4:
        return "Four"
    case 5:
        return "Five"
    case 6:
        return "Six"
    case 7:
        return "Seven"
    case 8:
        return "Eight"
    case 9:
        return "Nine"
    default:
        return ""
    }
}

func TestByLength(t *testing.T) {
    testCases := []struct {
        name     string
        input    []int
        expected []string
    }{
        {
            name: "Example1",
            input: []int{
                2, 1, 1, 4, 5, 8, 2, 3,
            },
            expected: []string{
                "Eight", "Five", "Four", "Three", "Two", "Two", "One", "One",
            },
        },
        {
            name: "Empty",
            input: []int{},
            expected: []string{},
        },
        {
            name: "IncludeStrange",
            input: []int{
                1, -1, 55,
            },
            expected: []