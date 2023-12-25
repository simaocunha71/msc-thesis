import (
    "strings"
)

// Given a string, find out how many distinct characters (regardless of case) does it consist of
// >>> CountDistinctCharacters('xyzXYZ')
// 3
// >>> CountDistinctCharacters('Jerry')
// 4
func CountDistinctCharacters(str string) int{
    count := 0
    for _, r := range str {
        if c, ok := strings.Split(r.ToString(), ""); len(c[1]) > len(count) {
            count = c[1]
        } else {
            count++
        }
    }
    return count + 1 // include character with zero occurences - this is not counted in the previous loop
}