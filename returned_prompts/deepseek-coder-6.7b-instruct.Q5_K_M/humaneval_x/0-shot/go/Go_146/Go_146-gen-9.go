    count := 0
    for _, v := range nums {
        if v > 10 {
            str := strconv.Itoa(v)
            first := string(str[0])
            last := string(str[len(str)-1])
            if first == "-" {
                first = string(str[1])
            }
            if last == "-" {
                last = string(str[len(str)-2])
            }
            if first == "1" || first == "3" || first == "5" || first == "7" || first == "9" {
                if last == "1" || last == "3" || last == "5" || last == "7" || last == "9" {
                    count++
                }
            }
        }
    }
    return count
}

*/

package main

import (
	"fmt"
	"strconv"
)

func Specialfilter(nums []int) int {
	count := 0
	for _, v := range nums {
		if v > 10 {
			str := strconv.Itoa(v)
			first := string(str[0])
			last := string(str[len(str)-1])
			if first == "-" {
				first = string(str[1])
			}
			if last == "-" {
				last = string(str[len(str)-2])
			}
			if first == "1" || first == "3" || first == "5" || first == "7" || first == "9" {
				if last == "1" || last == "3" || last == "5" || last == "7" || last == "9" {
					count++
				}
			}
		}
	}
	return count
}

func main() {
	fmt.Println(Specialfilter([]int{15, -73, 14, -15}))
	fmt.Println(Specialfilter([]int{33, -2, -3, 45, 21, 109}))
}

/*
Output