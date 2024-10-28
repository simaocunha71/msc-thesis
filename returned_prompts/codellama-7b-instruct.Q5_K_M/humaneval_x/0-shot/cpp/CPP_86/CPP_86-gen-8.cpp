/*
Write a function that takes a string and returns an ordered version of it.
Ordered version of string, is a string where all words (separated by space)
are replaced by a new word where all the characters arranged in
ascending order based on ascii value.
Note: You should keep the order of words and blank spaces in the sentence.

For example:
anti_shuffle("Hi") returns "Hi"
anti_shuffle("hello") returns "ehllo"
anti_shuffle("Hello World!!!") returns "Hello !!!Wdlor"
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){

    int j = 0;
    int i = 0;
    int count = 0;
    string newstring;
    string temp;
    while (s[j] != '\0'){
        j++;
        count++;
    }
    j = 0;
    i = 0;
    while (i < count){
        if (s[i] == ' '){
            temp = s.substr(j,i-j);
            j = i+1;
            sort(temp.begin(), temp.end());
            newstring += temp + " ";
        }
        i++;
    }
    temp = s.substr(j,i-j);
    sort(temp.begin(), temp.end());
    newstring += temp;
    return newstring;
}

int main(){
    string s;
    printf("Enter a string\n");
    getline(cin, s);
    printf("%s\n", anti_shuffle(s).c_str());
    return 0;
}
