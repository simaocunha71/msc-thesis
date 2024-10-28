
    for _, v := range lst1 {
        if v%2 != 0 {
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

import "fmt"

func Exchange(lst1, lst2 []int) string {

	for _, v := range lst1 {
		if v%2 != 0 {
			return "NO"
		}
	}

	return "YES"
}

func main() {
	fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 2, 3, 4}))
	fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 5, 3, 4}))
}




// This is a test

// This is another test

// And this is another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

// And another test

