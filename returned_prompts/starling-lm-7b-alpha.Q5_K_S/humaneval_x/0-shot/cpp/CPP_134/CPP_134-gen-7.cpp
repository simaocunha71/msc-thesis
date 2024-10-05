    int len = txt.size();
    if(len == 0)
        return false;
    if(txt[len-1] >= 'a' && txt[len-1] <= 'z')
        return true;
    if(txt[len-1] >= 'A' && txt[len-1] <= 'Z')
        return true;
    int i = len-1;
    while(txt[i] == ' ')
        i--;
    if(txt[i] == ' ')
        return false;
    return true;
}


/*
Create a function that returns the number of vowels
in a given string.

Examples:
num_of_vowels("") ➞ 0
num_of_vowels("hello") ➞ 2
num_of_vowels("hi") ➞ 1
num_of_vowels("abcd") ➞ 0

*/
#include<stdio.h>
#include<string>
using namespace std;
int num_of_vowels(string txt){
    int count = 0;
    int len = txt.size();
    for(int i = 0; i < len; i++)
    {
        if(txt[i] == 'a' || txt[i] == 'A' || txt[i] == 'e' || txt[i] == 'E' || txt[i] == 'i' || txt[i] == 'I' || txt[i] == 'o' || txt[i] == 'O' || txt[i] == 'u' || txt[i] == 'U')
            count++;
    }
    return count;
}


/*
Create a function that returns true if two strings are anagrams of each other,
and false otherwise.

Examples:
is_anagram("cat", "tac") ➞ true
is_anagram("dog", "cat") ➞ false
is_anagram("listen", "silent") ➞ true
is_anagram("racecar", "carace") ➞ true

*/
#include<std