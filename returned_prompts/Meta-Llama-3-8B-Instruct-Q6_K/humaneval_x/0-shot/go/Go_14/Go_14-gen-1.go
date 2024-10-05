    var prefixes []string
    for i := 0; i <= len(str); i++ {
        prefixes = append(prefixes, str[:i])
    }
    return prefixes
} //O(n^2) time complexity, O(n) space complexity. This function will return a list of all prefixes from shortest to longest of the input string. 

