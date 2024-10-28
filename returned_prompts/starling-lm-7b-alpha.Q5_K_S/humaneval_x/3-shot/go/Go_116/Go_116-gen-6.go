    type Number struct {
        value       int
        num_of_ones int
    }
    result := make([]Number, 0)
    for _, v := range arr {
        result = append(result, Number{value: v, num_of_ones: count_ones(v)})
    }
    sort.Slice(result, func(i, j int) bool {
        if result[i].num_of_ones != result[j].num_of_ones {
            return result[i].num_of_ones < result[j].num_of_ones
        }
        return result[i].value < result[j].value
    })

    result_arr := make([]int, 0)
    for _, v := range result {
        result_arr = append(result_arr, v.value)
    }
    return result_arr
}

func count_ones(n int) int {
    count := 0
    for n > 0 {
        if n%2 == 1 {
            count += 1
        }
        n /= 2
    }
    return count
}




// Run code to check the above solutions
package main

import "fmt"

func main() {
    fmt.Println(HasCloseElements([]float64{1.0, 2.0, 3.0}, 0.5))
    fmt.Println(HasCloseElements([]float64{1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3))
    fmt.Println(SeparateParenGroups("( ) (( )) (( )( ))"))
    fmt.Println(TruncateNumber(3.5))
    fmt.Println(SortArray([]int{1, 5, 2, 3, 4}))
    fmt.Println(SortArray([]int{-2, -3, -4, -5, -6}))
    fmt.Println(SortArray([]int{1, 0, 2, 3, 4}))
}





```