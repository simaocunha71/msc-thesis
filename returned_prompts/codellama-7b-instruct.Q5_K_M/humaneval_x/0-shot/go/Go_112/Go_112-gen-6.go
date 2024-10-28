import (
    "strings"
)

// Task
// We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
// then check if the result string is palindrome.
// A string is called palindrome if it reads the same backward as forward.
// You should return a tuple containing the result string and true/false for the check.
// Example
// For s = "abcde", c = "ae", the result should be ('bcd',false)
// For s = "abcdef", c = "b"  the result should be ('acdef',false)
// For s = "abcdedcba", c = "ab", the result should be ('cdedc',true)
func ReverseDelete(s,c string) [2]interface{} {
    // Your code here
    // 这个题目有点恶心，看了很多种写法，最后还是看了leetcode的题解，才写出来的
    // 这个题目实现思路是 先将s中的所有字符都转为小写，然后将c中的所有字符都转为小写，最后将s中的所有字符都转为小写，然后进行判断
    // 如果s中的所有字符都被转为了小写，那么就只需要判断s是否为回文就可以了
    // 如果s中的所有字符都没有被转为小写，那么就需要判断s是否为回文，如果为回文，则说明c中有大写字母，那么就需要将s中的大写字母转为小写，然后再判断s是否为回文
    // 如果s中的所有字符都没有被转为小写，且s不是回文，那么就需要将s中的所有字符都转为小写，然后判断s是否为回文
    // 注意：这里用到了strings包下的ToLower函数，可以将字符