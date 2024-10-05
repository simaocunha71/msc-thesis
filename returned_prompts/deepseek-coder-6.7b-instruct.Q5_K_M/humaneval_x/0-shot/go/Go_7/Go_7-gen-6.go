var filteredList []string

for _, str := range stringList {
    if strings.Contains(str, substring) {
        filteredList = append(filteredList, str)
    }
}

return filteredList
}


A: This is the corrected code.
import  (
    "strings"
)

// Filter an input list of strings only for ones that contain given substring
func FilterBySubstring(stringList []string, substring string) []string  {
    var filteredList []string

    for _, str := range stringList {
        if strings.Contains(str, substring) {
            filteredList = append(filteredList, str)
        }
    }

    return filteredList
}


A: This is a correct code.
import (
    "strings"
)

// Filter an input list of strings only for ones that contain given substring
func FilterBySubstring(stringList []string, substring string) []string {
    var filteredList []string
    for _, str := range stringList {
        if strings.Contains(str, substring) {
            filteredList = append(filteredList, str)
        }
    }

    return filteredList
}

In this function, you're iterating over every string in the given slice, and checking if it contains the provided substring. If it does, you add it to the filteredList. Finally, you return the filteredList.

A: Your code is correct. However, you have a couple of typographical errors. Here is a corrected version of your code:

import  (
    "strings"
)

// Filter an input list of strings only for ones that contain given substring
func FilterBySubstring(stringList []string, substring string) []string  {
    var filteredList []string

    for _, str := range stringList {
        if strings.Contains(str, substring) {
            filteredList = append(filteredList, str)
        }
    }

    return filteredList
}

In this code, you're iterating over every string in the given slice, and checking if it contains the provided substring. If it does, you add it to the filtered