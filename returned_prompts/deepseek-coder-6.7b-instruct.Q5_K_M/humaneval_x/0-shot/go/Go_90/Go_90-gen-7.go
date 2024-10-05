    if len(lst) < 2 {
        return nil
    }

B:
    sort.Ints(lst)

C:
    for i := 1; i < len(lst); i++ {
        if lst[i] > lst[0] {
            return lst[i]
        }
    }

D:
    return nil
}

*/

package main

import (
	"fmt"
	"sort"
)

func NextSmallest(lst []int) interface{} {
	if len(lst) < 2 {
		return nil
	}

	sort.Ints(lst)

	for i := 1; i < len(lst); i++ {
		if lst[i] > lst[0] {
			return lst[i]
		}
	}

	return nil
}

func main() {
	fmt.Println(NextSmallest([]int{1, 2, 3, 4, 5}))  // 2
	fmt.Println(NextSmallest([]int{5, 1, 4, 3, 2}))  // 2
	fmt.Println(NextSmallest([]int{}))               // nil
	fmt.Println(NextSmallest([]int{1, 1}))           // nil
}

// Output:
// 2
// 2
// <nil>
// <nil>

// Explanation:
// For the first test case, the 2nd smallest element is 2.
// For the second test case, the 2nd smallest element is 2.
// For the third test case, there are no elements, so there is no 2nd smallest element.
// For the fourth test case, all elements are the same, so there is no 2nd smallest element.

// Time complexity: O(n log n) due to sorting
// Space complexity: O(1) since we are using constant extra space
