
for i := range lst1{
    if lst1[i] % 2 != 0 {
        for j := range lst2{
            if lst2[j] % 2 == 0 {
                lst1[i], lst2[j] = lst2[j], lst1[i]
                break
            }
        }
    }
}

for i := range lst1{
    if lst1[i] % 2 != 0 {
        return "NO"
    }
}
return "YES"

}

func main() {
fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 2, 3, 4}))
fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 5, 3, 4}))
}

*/

package main

import "fmt"

// Exchange function
func Exchange(lst1, lst2 []int) string {
	for i := range lst1 {
		if lst1[i]%2 != 0 {
			for j := range lst2 {
				if lst2[j]%2 == 0 {
					lst1[i], lst2[j] = lst2[j], lst1[i]
					break
				}
			}
		}
	}

	for i := range lst1 {
		if lst1[i]%2 != 0 {
			return "NO"
		}
	}
	return "YES"
}

func main() {
	fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 2, 3, 4}))
	fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 5, 3, 4}))
}

// ----------------

// If the list lst1 has an odd number and lst2 has an even number,
// switch them and