
// Write a function that takes a list of strings and returns a list of unique strings without case sensitivity.
// 
// Examples
// unique_strings(['hello', 'world', 'Hello', 'WORLD']) ➞ ['hello', 'world']
// unique_strings(['apple', 'BANANA', 'orange', 'ORANGE']) ➞ ['apple', 'banana', 'orange']
// unique_strings(['cODe', 'wItH', 'cOde', 'wItH']) ➞ ['code', 'with']
// unique_strings(['hello', 'HELLO']) ➞ ['hello']
// unique_strings(['hello', 'world', 'HELLO', 'WORLD']) ➞ ['hello', 'world']
func unique_strings(lst []string) []string {

B:

// Write a function that takes a list of integers and returns a list of unique integers without order.
// 
// Examples
// unique_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
// unique_integers([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) ➞ [1, 2, 3, 4, 5]
// unique_integers([1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) ➞ [1, 2]
// unique_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 