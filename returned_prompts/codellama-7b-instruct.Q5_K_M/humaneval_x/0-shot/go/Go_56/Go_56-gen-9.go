
// 1. for every opening bracket, find the corresponding closing bracket.
// 2. if there is no closing bracket, return false.
// 3. if there is no opening bracket, return false.
// 4. if there is a closing bracket, but there's already a closing bracket for that opening bracket, return false.
// 5. return true

var openingBrackets []int
var closingBrackets []int

for i := 0; i < len(brackets