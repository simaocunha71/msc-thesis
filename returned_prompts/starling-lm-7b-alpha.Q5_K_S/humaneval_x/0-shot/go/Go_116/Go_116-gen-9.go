    type Pair struct {
        val  int
        ones int
    }

    pairs := make([]Pair, len(arr))
    for i, val := range arr {
        pairs[i] = Pair{val, countOnes(val)}
    }
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].ones == pairs[j].ones {
            return pairs[i].val < pairs[j].val
        }
        return pairs[i].ones < pairs[j].ones
    })

    ret := make([]int, len(arr))
    for i, p := range pairs {
        ret[i] = p.val
    }
    return ret
}

func countOnes(num int) int {
    count := 0
    for num > 0 {
        if num%2 == 1 {
            count++
        }
        num /= 2
    }
    return count
}

/*
Now let's test the function:
*/

func main() {
    fmt.Println(SortArray([]int{1, 0, 2, 3, 4})) // []int
    fmt.Println(SortArray([]int{-2, -3, -4, -5, -6})) // []int
    fmt.Println(SortArray([]int{1, 5, 2, 3, 4})) // []int
}












































































































































































