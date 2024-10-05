import (
    "strings"
)

// Create a function which takes a string representing a file's name, and returns
// 'Yes' if the the file's name is valid, and returns 'No' otherwise.
// A file's name is considered to be valid if and only if all the following conditions
// are met:
// - There should not be more than three digits ('0'-'9') in the file's name.
// - The file's name contains exactly one dot '.'
// - The substring before the dot should not be empty, and it starts with a letter from
// the latin alphapet ('a'-'z' and 'A'-'Z').
// - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
// Examples:
// FileNameCheck("example.txt") # => 'Yes'
// FileNameCheck("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
func FileNameCheck(file_name string) string {
    var result string
    var err error
    var count int
    var flag bool
    var flag1 bool
    var flag2 bool
    var flag3 bool
    var flag4 bool
    var flag5 bool
    var flag6 bool
    var flag7 bool
    var flag8 bool
    var flag9 bool
    var flag10 bool
    var flag11 bool
    var flag12 bool
    var flag13 bool
    var flag14 bool
    var flag15 bool
    var flag16 bool
    var flag17 bool
    var flag18 bool
    var flag19 bool
    var flag20 bool
    var flag21 bool
    var flag22 bool
    var flag23 bool
    var flag24 bool
    var flag25 bool
    var flag26 bool
    var flag27 bool
    var flag28 bool
    var flag29 bool
    var flag30 bool
    var flag31 bool
    var flag32 bool
    var flag33 bool
    var flag34 bool
    var flag35 bool
    var flag36 bool
    var flag37 bool
   