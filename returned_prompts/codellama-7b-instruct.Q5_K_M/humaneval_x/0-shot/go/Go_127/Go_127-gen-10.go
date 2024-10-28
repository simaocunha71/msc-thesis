
// Given two non-negative integers a and b,
// your task is to calculate the number of trailing zeros in the factorial of a+b.
// The factorial of an integer is calculated as follows: 5! = 5 × 4 × 3 × 2 × 1,
// or in mathematical notation: 5! = 5 × (5 − 1) × (5 − 2) × ... × 1.
// The number of trailing zeros in the factorial of an integer is the number of
// zeros that are found at the end of the integer when it is written in its
// prime factorization. For example, the number of trailing zeros in 120 is 2,
// because 120 = 2 × 2 × 3 × 5 × 5, and there are two factor pairs of the form 5 × 5.
// However, the number of trailing zeros in 125 is 0, because 125 = 5 × 5 × 5 × 5 × 5,
// and there are no factor pairs of the form 5 × 5.
// Given two non-negative integers a and b,
// your task is to calculate the number of trailing zeros in the factorial of a+b.
// 
// 
// [input/output] samples:
// TrailingZeros(10, 10) ==> 2
// TrailingZeros(3, 10) ==> 0
// TrailingZeros(3, 3) ==> 1
func TrailingZeros(a, b int) int {

B:

// You are given a string consisting of a single character repeated
// a non-negative integer number of times.
// For example, "a1000" is a valid string, and it represents the string "aaaaa".
// Your task is to return the string that is contained in the given string.
// 
// 
// [input/output] samples:
// Repeat("a", 0) ==> ""
// Repeat("a", 1) ==> "a"
// Repeat("a", 10) ==> "aaaaaaaaaa"
func Repeat(character string, n int) string {

C:

// You