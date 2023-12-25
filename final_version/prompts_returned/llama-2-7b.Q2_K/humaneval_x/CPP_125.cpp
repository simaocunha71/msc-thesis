/*
Given a string of words, return a vector of words split on whitespace, if no whitespaces exists in the text you
should split on commas ',' if no commas exists you should return a vector with one element, the number of lower-case letters with odd order in the
alphabet, ord("a") = 0, ord("b") = 1, ... ord("z") = 25
Examples
split_words("Hello world!") ➞ {"Hello", "world!"}
split_words("Hello,world!") ➞ {"Hello", "world!"}
split_words("abcdef") == {"3"} 
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> split_words(string txt){
	int index = 0, n = 1;
    vector < string > result;
    
    int i=0;                 // iterates through the txt.
    while (i != -1) {           // if a space exists, then adds the word to the arraylist and decrements count of spaces by one.
        if(txt[index] == ' ')      // checks for spaces
            n--;                     // subtracts 1 from count of spaces
	    else {                       // if a space does not exist, then adds the word in the vector to store words in txt.
            result.push_back(txt[i]);   // adds the word to the arraylist
        	printf("%c",txt[i]); 
        }
        i++;      // iterates to next index.
    }
}
int main() {
     string text;
    cout <<"Enter a phrase in English (without spaces):";
    cin >>text;                            // reads string as input from user.  
    split_words(text);                       // splits the given string into words using space as the delimiter, and adds them to the vector of strings.
      return 0;
}
