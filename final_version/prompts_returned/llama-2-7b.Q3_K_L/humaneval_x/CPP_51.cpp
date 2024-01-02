/*
remove_vowels is a function that takes string and returns string without vowels.
>>> remove_vowels("")
""
>>> remove_vowels("abcdef\nghijklm")
"bcdf\nghjklm"
>>> remove_vowels("abcdef")
"bcdf"
>>> remove_vowels("aaaaa")
""
>>> remove_vowels("aaBAA")
"B"
>>> remove_vowels("zbcd")
"zbcd"
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string remove_vowels(string text){
	int index = 0, count = 0;
    for(int i=0;i<text.length();++i)
        if (isalpha(text[i]) == false && isdigit(text[i])==false )
            ++count;
        else{
            text[index] = text[i];
	    index++;
             }
    return text.substr(0,index);
}
