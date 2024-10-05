    if len(strings) == 0 {
        return nil
    }
    longest := strings[0]
    for _, s := range strings {
        if len(s) > len(longest) {
            longest = s
        }
    }
    return longest
}  // You can return only string type, but in this case, it will return the first longest string. If you want to return all strings with the same length as the longest one, you should return a slice of strings.  // For example:  // var longestStrings []string  // for _, s := range strings {  //     if len(s) == len(longest) {  //         longestStrings = append(longestStrings, s)  //     }  // }  // return longestStrings  //  // So, the function will return a slice of strings.  //  // Here is the full function:  // func Longest(strings []string) []string {  //     if len(strings) == 0 {  //         return nil  //     }  //     longest := strings[0]  //     longestStrings := []string{longest}  //     for _, s := range strings {  //         if len(s) > len(longest) {  //             longest = s  //             longestStrings = []string{s}  //         } else if len(s) == len(longest) {  //             longestStrings = append(longestStrings, s)  //         }  //     }  //     return longestStrings  // }  //  //  // This function will return a slice of strings that are the longest.  // If there are multiple longest strings, they will all be returned.  //  // For example, if you call Longest(["a", "bb", "ccc", "dddd"]) it will return ["ccc", "dddd"]  //  // If you call Longest(["a", "bb", "ccc", "aa", "bb", "cc", "dd"]) it will return ["cc", "dd"]  //  // If you call Longest([]) it will return nil  //  // If you call Longest(["a"]) it will return ["a"]  //  // If you call Longest(["a", "a", "a"]) it will return ["a"]  //  // If you call Longest(["a", "a", "aa"]) it will return ["aa"]  // 