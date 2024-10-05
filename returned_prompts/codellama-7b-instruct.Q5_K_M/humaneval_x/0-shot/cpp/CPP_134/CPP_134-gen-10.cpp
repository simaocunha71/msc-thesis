/*
Create a function that returns the index of the last
occurence of a given character in a given string.
If the character is not found, return -1.

Examples:
last_index_of("hello world", "l") ➞ 8
last_index_of("hello world", "z") ➞ -1
*/
#include <iostream>
using namespace std;
int last_index_of(string str, char ch) {
int last_index = -1;
for(int i = 0; i < str.length(); i++) {
    if(str[i] == ch) {
        last_index = i;
    }
}
return last_index;
}

