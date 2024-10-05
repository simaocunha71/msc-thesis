
	var res []int
    for _, v := range values {
        if val, ok := v.(int); ok {
            res = append(res, val)
        }
    }
    return res
}

*/

package main

import "fmt"

func FilterIntegers(values []interface{}) []int {
	var res []int
	for _, v := range values {
		if val, ok := v.(int); ok {
			res = append(res, val)
		}
	}
	return res
}

func main() {
	fmt.Println(FilterIntegers([]interface{}{'a', 3.14, 5}))
	fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", make(map[string]int), []int{}}))
}
