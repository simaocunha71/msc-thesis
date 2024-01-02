import (
    "sort"
)

// Write a function that accepts a list of strings as a parameter,
// deletes the strings that have odd lengths from it,
// and returns the resulted list with a sorted order,
// The list is always a list of strings and never an array of numbers,
// and it may contain duplicates.
// The order of the list should be ascending by length of each word, and you
// should return the list sorted by that rule.
// If two words have the same length, sort the list alphabetically.
// The function should return a list of strings in sorted order.
// You may assume that all words will have the same length.
// For example:
// assert list_sort(["aa", "a", "aaa"]) => ["aa"]
// assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
func SortedListSum(lst []string) []string {
    // sort by length, then alphabetically if equal.  return unique sorted results
    sort.Strings = func(i, j int) bool {
        a := len(strings[i])
        b := len(strings[j])
        if a == b && strings[i] != strings[j] {
            return strings[i] < strings[j]
        } else if a > b || strings[i] == "aa" {
            return true
        } else if a < b || strings[i] == "bb" {
            return false
        } else {
            return a < b
        }
    }
    return sorted_list(lst)
}
