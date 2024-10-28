
// Filter an input list of integers, returning only those that are greater than a given value.
// >>> FilterGT([]int{}, 3)
// []
// >>> FilterGT([]int{1, 2, 3, 4, 5}, 3)
// [4, 5]
func FilterGT(ints []int, n int) []int {

B:

// Return the sum of the digits of a positive integer.
// >>> SumDigits(12345)
// 15
// >>> SumDigits(99)
// 18
func SumDigits(n int) int {

C:

// Given a dictionary of words, return a list of all words that can be formed by
// a sequence of other words in the dictionary.
// >>> FindSequence(['cat', 'dog', 'apple', 'banana', 'cherry', 'dad', 'daughter', 'father', 'mother'])
// ['cat dog', 'cat dog apple', 'cat dog banana', 'cat dog cherry', 'cat dog daughter', 'cat dog father', 'cat dog mother', 'cat daughter', 'cat daughter father', 'cat daughter mother', 'cat father', 'cat father mother', 'cat mother', 'dog apple', 'dog banana', 'dog cherry', 'dog daughter', 'dog father', 'dog mother', 'apple banana', 'apple cherry', 'apple daughter', 'apple father', 'apple mother', 'banana cherry', 'banana daughter', 'banana father', 'banana mother', 'cherry daughter', 'cherry father', 'cherry mother', 'dad apple', 'dad banana', 'dad cherry', 'dad daughter', 'dad father', 'dad mother', 'daughter father', 'daughter mother', 'father mother']
func FindSequence(dict map[string]bool) []string {

D:

// Return the number of bits required to represent an integer n in binary.
// >>> NumBits(0)
// 1
// >>> NumBits(1)
// 1
// >>> NumBits(2)
// 2
// >>> NumBits(3)
// 2
// >>> NumBits(