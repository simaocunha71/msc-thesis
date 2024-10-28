
// You are given a string which contains only lowercase letters, and a target
// string. Your task is to find all the start indices of the target string in
// the given string.
// For example, given the string "abpple" and the target string "pp",
// return the index [1, 4].
// You may assume that the target string is a non-empty substring and
// could occur more than once in the given string.
// 
// 
// [input/output] samples:
// find_all_indexes("abpple", "pp") ==> [1, 4]
// find_all_indexes("abpple", "b") ==> [2]
// find_all_indexes("abpple", "e") ==> []
func find_all_indexes(string string, target string) []int {

B:

// You are given a list of integers and two integers, a and b.
// Your task is to find all integers in the list that fall in the range
// [a, b] inclusive. Return the answer in any order.
// 
// 
// [input/output] samples:
// get_range([1, 2, 3, 4, 5], 2, 4) ==> [2, 3]
// get_range([1, 2, 3, 4, 5], 2, 6) ==> [2, 3, 4]
// get_range([1, 2, 3, 4, 5], 1, 5) ==> [1, 2, 3, 4, 5]
func get_range(list []int, a, b int) []int {

C:

// You are given a string and a pattern. Your task is to find all the start
// indices of the pattern in the given string.
// For example, given the string "ababab" and the pattern "ab", return the
// index [0, 1, 2, 3].
// You may assume that the pattern is a non-empty substring of the given string.
// 
// 
// [input/output] samples:
// find_all_indexes("ababab",