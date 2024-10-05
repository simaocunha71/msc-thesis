    sort.Ints(array)

B:
    if sum % 2 == 0 {
        return array
    } else {
        sort.Sort(sort.Reverse(sort.IntSlice(array)))
    }

    return array
}

C:
    if len(array) == 0 {
        return array
    }

    if array[0] > array[len(array) - 1] {
        sort.Sort(sort.Reverse(sort.IntSlice(array)))
    } else {
        sort.Ints(array)
    }

    return array
}

D:
    if array[0] + array[len(array) - 1] % 2 == 0 {
        sort.Ints(array)
    } else {
        sort.Sort(sort.Reverse(sort.IntSlice(array)))
    }

    return array
}

E:
    sort.Ints(array)

    if array[0] + array[len(array)-1] % 2 == 0 {
        return array
    } else {
        sort.Sort(sort.Reverse(sort.IntSlice(array)))
    }

    return array
}
*/

import (
	"sort"
)

// Given an array of non-negative integers, return a copy of the given array after sorting,
// you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
// or sort it in descending order if the sum( first index value, last index value) is even.
// 
// Note:
// 1. don't change the given array.
// 
// Examples:
// * SortArray([]) 					=> []
// * SortArray([5]) 					=>