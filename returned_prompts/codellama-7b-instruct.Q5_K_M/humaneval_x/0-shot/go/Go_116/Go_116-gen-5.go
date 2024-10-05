import (
    "fmt"
    "sort"
)

func SortArray(arr []int) []int {
    type pair struct {
        x, y int
    }

    pairs := make([]pair, len(arr))
    for i, v := range arr {
        pairs[i] = pair{v, bits.OnesCount(uint(v))}
    }

    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].y == pairs[j].y {
            return pairs[i].x < pairs[j].x
        }
        return pairs[i].y < pairs[j].y
    })

    result := make([]int, len(arr))
    for i, p := range pairs {
        result[i] = p.x
    }
    return result
}
