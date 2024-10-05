
// Concatenate list of integers into a single integer
// >>> Concatenate([])
// 0
// >>> Concatenate([1, 2, 3])
// 123
func Concatenate(integers []int) int {

B:

// Concatenate list of booleans into a single boolean
// >>> Concatenate([])
// false
// >>> Concatenate([true, false, true])
// true
func Concatenate(booleans []bool) bool {

C:

// Concatenate list of floats into a single float
// >>> Concatenate([])
// 0.0
// >>> Concatenate([1.1, 2.2, 3.3])
// 1.12.23.3
func Concatenate(floats []float64) float64 {

D:

// Concatenate list of characters into a single character
// >>> Concatenate([])
// ''
// >>> Concatenate(['a', 'b', 'c'])
// 'abc'
func Concatenate(chars []rune) rune {

E:

// Concatenate list of bytes into a single byte
// >>> Concatenate([])
// ''
// >>> Concatenate([0x00, 0x01, 0x02])
// '000102'
func Concatenate(bytes []byte) byte {

F:

// Concatenate list of arrays into a single array
// >>> Concatenate([])
// []
// >>> Concatenate([[1, 2, 3], [4, 5, 6]])
// [1, 2, 3, 4, 5, 6]
func Concatenate(arrays [][]int) []int {

G:

// Concatenate list of slices into a single slice
// >>> Concatenate([])
// []
// >>> Concatenate([[1, 2, 3], [4, 5, 6]])
// [1, 2, 3, 4, 5, 6]
func Concatenate(slices [][]int)