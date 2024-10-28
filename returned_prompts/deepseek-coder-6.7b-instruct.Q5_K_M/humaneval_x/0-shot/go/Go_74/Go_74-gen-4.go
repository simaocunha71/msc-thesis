
    total1 := 0
    total2 := 0

    for _, v := range lst1 {
        total1 += len(v)
    }

    for _, v := range lst2 {
        total2 += len(v)
    }

    if total1 < total2 {
        return lst1
    } else if total1 > total2 {
        return lst2
    } else {
        return lst1
    }
}

*/

package main

import (
	"fmt"
)

func TotalMatch(lst1 []string, lst2 []string) []string {
	total1 := 0
	total2 := 0

	for _, v := range lst1 {
		total1 += len(v)
	}

	for _, v := range lst2 {
		total2 += len(v)
	}

	if total1 < total2 {
		return lst1
	} else if total1 > total2 {
		return lst2
	} else {
		return lst1
	}
}

func main() {
	fmt.Println(TotalMatch([]string{}, []string{}))
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "Hi"}))
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hi", "hi", "admin", "project"}))
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "hi", "hi"}))
	fmt.Println(TotalMatch([]string{"4"}, []string{"1", "2", "3", "4", "5"}))
}

// Output:
// []
// [hI Hi]
// [hi admin]
// [hI hi hi]
// [4]
// Expected output:
// []
// [hI Hi]
// [hi admin]
// [hI hi hi]
// [4]
/*
