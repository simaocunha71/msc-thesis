
// Return a string of all the digits of the integer x.
// >>> AllDigits(12345)
// "12345"
// >>> AllDigits(123456789)
// "123456789"
func AllDigits(x int) string {

B:

// Return the number of digits of the integer x.
// >>> NumDigits(12345)
// 5
// >>> NumDigits(123456789)
// 9
func NumDigits(x int) int {

C:

// Return the integer y such that the last digit of x is the first digit
// of y, and the second last digit of x is the second digit of y, and so on.
// >>> LastDigits(12345, 1)
// 2345
// >>> LastDigits(12345, 2)
// 345
// >>> LastDigits(12345, 3)
// 45
// >>> LastDigits(12345, 4)
// 5
// >>> LastDigits(12345, 5)
// 5
func LastDigits(x, y int) int {

D:

// Return the integer y such that the first digit of x is the last digit
// of y, and the second digit of x is the second last digit of y, and so on.
// >>> FirstDigits(12345, 1)
// 5
// >>> FirstDigits(12345, 2)
// 45
// >>> FirstDigits(12345, 3)
// 345
// >>> FirstDigits(12345, 4)
// 2345
// >>> FirstDigits(12345, 5)
// 12345
func FirstDigits(x, y int) int {

E:

// Return the integer y such that the first digit of x is the first digit
// of y, and the second digit of x is the second digit