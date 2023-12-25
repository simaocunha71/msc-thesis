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
    var lst1 []string = make([]string, 0, len(lst))

    if !reflect.DeepEqual(lst, lst1) {
        for _, element := range lst {
            switch element {
            case "a":
                lst1 = append(lst1, element)
            case "b":
                lst1 = append(lst1, element)
            default:
                continue
            }
        }
    } else {
        return []string{}
    }

    for _, element := range lst1 {
        switch element {
        case "a":
            break
        case "b":
            break
        default:
            continue
        }
    }

    switch listSum(lst) {
    case 0: // "a"
        return []string{
            "a",
        }
    case 1: // "b" or "a"
        return []string{
            "a",
            "b",
        }
    default: // "aa" or "bb" with the last one sorted alphabetically.
        return []string{
            "a",
            "b",
        }
    }

    for _, element := range lst1 {
        switch element {
        case "a":
            break