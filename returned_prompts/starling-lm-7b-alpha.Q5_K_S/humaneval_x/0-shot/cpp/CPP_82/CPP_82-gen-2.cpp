    int len = str.length();
    if(len == 1) return true;
    if(len == 2) return true;
    if(len == 3) return true;
    if(len % 2 == 0) return false;
    for(int i = 3; i <= len / 2; i += 2) {
        if(len % i == 0) {
            return false;
        }
    }
    return true;
}


/*
Write a function that takes a string and returns true if all the
characters in the string are unique or false otherwise
Examples
unique_characters("Hello") == true
unique_characters("abcdcba") == false
unique_characters("kittens") == false
unique_characters("orange") == true
*/
#include<stdio.h>
#include<string>
using namespace std;
bool unique_characters(string str){
    char c[300] = {0};
    int len = str.length();
    for(int i = 0; i < len; i++) {
        if(c[str[i]] == 0) {
            c[str[i]] = 1;
        } else {
            return false;
        }
    }
    return true;
}


/*
Write a function that takes a string and returns true if the string
is a palindrome or false otherwise
Examples
palindrome("racecar") == true
palindrome("hello") == false
palindrome("mom") == true
palindrome("civic") == true
*/
#include<stdio.h>
#include<string>
using namespace std;
bool palindrome(string str){
    int len = str.length();
    for(int i = 0; i < len / 2; i++) {
        if(str[i] != str[len - i - 1]) {
            return false;
        }
    }
    return true;
}


/*
Write a function that takes an array of integers and returns the
sum of all the elements in the array
Examples
sum_