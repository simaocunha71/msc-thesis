//You are given an integer N. Find the smallest positive integer M such that N*M is a palindrome.
#include<stdio.h>
#include<math.h>
using namespace std;
int smallest_palindrome(int n){
B:
/*
Given a string s, find the minimum number of characters you need to delete to make s a palindrome.
For example:
min_deletions("aaabb") == 2 // Remove the two outer 'a's
min_deletions("abdba") == 0  // Already a palindrome
min_deletions("abdba") == 0  // Already a palindrome
*/
#include<stdio.h>
#include<math.h>
#include<string.h>
using namespace std;
int min_deletions(char *s){
C:
/*
Given a string s and a set of characters t, find the minimum number of characters you need to remove
from s to make it a t-palindrome. A string is a t-palindrome if it reads the same forwards and backwards,
and it only contains characters from the set t.

For example:
min_deletions("abcba", {"a", "b", "c"}) == 0 // Already a palindrome
min_deletions("abba", {"a", "b", "c"}) == 2 // Remove the 'b's and 'c's
min_deletions("abcde", {"a", "b", "c"}) == 4 // Remove all the characters
*/
#include<stdio.h>
#include<math.h>
#include<string.h>
using namespace std;
int min_deletions(char *s, vector<char> t){
D:
/*
Given a string s, find the minimum number of characters you need to change to make s a palindrome.
For example:
smallest_change("abcba") == 0 // Already a palindrome
smallest_change("abcde") == 1 // Change the last 'e' to 'd'
smallest_change("abcde") == 1 // Change the last 'e' to 'd'
*/
#include<stdio.h>
#include<math.h>
#include<string.h>
using namespace std;
int smallest_change(char *s){
E:
/*
Given a string s and a set of characters t, find the minimum number of characters you need to change
to make s a t-palindrome. A string is a t-palindrome if it reads the same forwards and backwards,
and it only contains characters from the set t.

For example:
smallest_change("abcba", {"a