/*
Write a function that takes a string as input and returns the first non-repeating character in the string.
>>> firstNonRepeating("abacabad")
'b'
>>> firstNonRepeating("leetcode")
't'
*/
#include<stdio.h>
#include<stdlib.h>
using namespace std;
char firstNonRepeating(string str){
    int i,j;
    int a[26]={0};
    for(i=0;i<str.length();i++){
        a[str[i]-'a']++;
    }
    for(i=0;i<str.length();i++){
        if(a[str[i]-'a']==1){
            return str[i];
        }
    }
    return 'a