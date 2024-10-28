    if (txt.empty())
        return false;
    int i = txt.size() - 1;
    while (i >= 0 && txt[i] != ' ')
        --i;
    return i >= 0 && ('a' <= txt[i] && txt[i] <= 'z') || ('A' <= txt[i] && txt[i] <= 'Z');
}

/*
Create a function that takes a string as input and returns the
length of the longest substring in the string that is made of only
lowercase letters.

Examples:
longest_lowercase_substring("hello, world!") ➞ 5
longest_lowercase_substring("abcde") ➞ 5
longest_lowercase_substring("abcDEf") ➞ 0
*/

#include<algorithm>
#include<iostream>
#include<string>
using namespace std;
int longest_lowercase_substring(string str) {
    int len = str.length();
    int result = 0;
    for (int i = 0; i < len; i++) {
        int j = i;
        while (j < len && 'a' <= str[j] && str[j] <= 'z') {
            j++;
        }
        result = max(result, j - i);
        i = j;
    }
    return result;
}

/*
Create a function that takes a string as input and returns a string
that is the reversal of the input string.

Examples:
reverse_string("Hello") ➞ "olleH"
reverse_string("Goodbye") ➞ "eyboodG"
reverse_string("") ➞ ""
*/

#include<iostream>
#include<string>
using namespace std;
string reverse_string(string txt) {
    string result = "";
    for (int i = txt.length() - 1; i >= 0; i--) {
        result += txt[i];
    }
    return result;
}

/*
Create a function that takes a string as input and returns a string
that is the reversal of the