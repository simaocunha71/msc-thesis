    sort.Ints(l1)
    sort.Ints(l2)

B:
    l1 = unique(l1)
    l2 = unique(l2)

C:
    var common []int

D:
    for _, i := range l1 {
        if contains(l2, i) {
            common = append(common, i)
        }
    }

E:
    return common
}

func unique(intSlice []int) []int {

F:
    keys := make(map[int]bool)
    list := []int{}

G:
    for _, entry := range intSlice {
        if _, value := keys[entry]; !value {
            keys[entry] = true
            list = append(list, entry)
        }
    }

H:
    return list
}

func contains(s []int, e int) bool {

I:
    for _, a := range s {
        if a == e {
            return true
        }
    }

J:
    return false
}


A: This program returns the common elements in two lists after sorting them.

B: The unique function removes duplicates in the list.

C: The common variable is declared to store the common elements.

D: This loop compares each element in l1 with l2. If there is a common element, it appends it to the common slice.

E: The sorted unique common elements are returned.

F: keys is a map to check for duplicate elements.

G: For every element in the intSlice, if the element is not in the keys map, it appends the element to the list and adds the element to the keys map.

H: The list without duplicates is returned.

I: This loop checks if the element e is in the slice s. If it is, the function returns true. If not, it returns false.

J: The function contains checks whether element e is in the slice s. If it is, it returns true. If not, it returns false.

*/
package main

import (
	"fmt"
)

func main() {
	f