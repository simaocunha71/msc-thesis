    for _, v := range arr {
        if v < 0 {
            v = -v
        }
    }
    type pair struct {
        val  int
        ones int
    }
    a := make([]pair, len(arr))
    for i, v := range arr {
        a[i] = pair{val: v, ones: count(v)}
    }
    sort.Slice(a, func(i, j int) bool {
        if a[i].ones == a[j].ones {
            return a[i].val < a[j].val
        }
        return a[i].ones < a[j].ones
    })
    for i, v := range a {
        arr[i] = v.val
    }
    return arr
}

func count(n int) int {
    c := 0
    for n > 0 {
        if n%2 == 1 {
            c++
        }
        n /= 2
    }
    return c
}

*/
This solution first counts the number of ones in the binary representation of each integer in the array. It then sorts the integers according to the number of ones in their binary representation, with ties broken by the decimal value.

func count(n int) int {
    c := 0
    for n > 0 {
        if n%2 == 1 {
            c++
        }
        n /= 2
    }
    return c
}

func SortArray(arr []int) []int {
    for _, v := range arr {
        if v < 0 {
            v = -v
        }
    }
    type pair struct {
        val  int
        ones int
    }
    a := make([]pair, len(arr))
    for i, v := range arr {
        a[i] = pair{val: v, ones: count(v)}
    }
    sort.Slice(a, func(i, j int) bool {
        if a[i].ones == a[j].ones {
            return a[i].val < a[j].val
        }
        return a[i].ones < a[j