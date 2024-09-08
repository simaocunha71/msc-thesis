/*
Write a function vowels_count which takes a string representing a word as input and returns the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
Here, 'y' is also a vowel, but only when it is at the end of the given word.
Example: 
>>> vowels_count("abcde") 
2 
>>> vowels_count("ACEDY") 
3
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
int vowels_count(string s){
    int count=0;
    for(int i=0;i<s.size();i++){
        if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'||s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U'||s[i]=='y'||s[i]=='Y'){
            count++;
        }
    }
    if(s[s.size()-1]=='y'||s[s.size()-1]=='Y'){
        count--;
    }
    return count;
}