```go
func IntToMiniRoman(number int) string {
    romanMap := map[int]string{
        1000: "m",
        900: "cm",
        500: "d",
        400: "cd",
        100: "c",
        90: "xc",
        50: "l",
        40: "xl",
        10: "x",
        9: "ix",
        5: "v",
        4: "iv",
        1: "i",
    }
    result := ""
    for _, value := range sort.IntSlice(mapKeys(romanMap)) {
        for number >= value {
            number -= value
            result += romanMap[value]
        }
    }
    return strings.ToLower(result)
}

func mapKeys(m map[int]string) []int {
    keys := make([]int, 0, len(m))
    for k := range m {
        keys = append(keys, k)
    }
    return keys
}
```

Explanation:
This function takes an integer as input and returns its roman numeral equivalent as a string in lowercase. It uses a map to store the roman numeral values and their corresponding integer values. The function iterates over the sorted keys of the map and subtracts the value from the input number as long as it is greater than or equal to the value. It then appends the corresponding roman numeral to the result string. The function finally returns the result string in lowercase using the `strings.ToLower` function.

The `mapKeys` function is used to get the keys of the map in a sorted order, which is necessary for the iteration process.

The time complexity of this function is O(n), where n is the number of entries in the map, and the space complexity is O(n) for storing the result string.