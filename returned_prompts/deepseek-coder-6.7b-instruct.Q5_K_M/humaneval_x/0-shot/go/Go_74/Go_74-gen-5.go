
    len1 := sumChars(lst1)
    len2 := sumChars(lst2)
    
    if len1 < len2 {
        return lst1
    } else if len1 > len2 {
        return lst2
    }
    return lst1
}

func sumChars(lst []string) (total int) {
    for _, word := range lst {
        total += len(word)
    }
    return total
}

This function first calculates the total number of characters in each list using the helper function sumChars. It then compares these totals and returns the list with the smaller total. If the totals are equal, it returns the first list.

In the example TotalMatch(['hi',  'admin'],  ['hI',  'Hi']), the total number of characters in the first list is 6 and the total number of characters in the second list is 4, so the function returns the first list ['hI',  'Hi'].

In the example TotalMatch(['hi',  'admin'],  ['hi',  'hi',  'admin',  'project']), the total number of characters in the first list is 18 and the total number of characters in the second list is 14, so the function returns the second list ['hi',  'hi',  'admin',  'project'].

In the example TotalMatch(['4'],  ['1',  '2',  '3',  '4',  '5']), the total number of characters in the first list is 1 and the total number of characters in the second list is 14, so the function returns the first list ['4'].

In the example TotalMatch([],  []), the total number of characters in both lists is 0, so the function returns an empty list [].

I hope this helps. Let me know if you have any other questions.
*/

package main

import (
	"fmt"
)

func TotalMatch(lst1 []string, lst2 []string) []string {

	len1 := sumChars(lst1)
	len2 := sumChars(lst2)

	if len1 < len2 {
	