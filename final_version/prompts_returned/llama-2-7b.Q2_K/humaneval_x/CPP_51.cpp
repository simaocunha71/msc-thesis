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
	int count = 0;
	for (int i=0,j;i<text.size();++i) { // loop over the string `text'
		if (!isalpha(text[i])){
			continue;
		}
		if (isalnum(text[i]) && !isspace(text[i], ':', '+')){
			count++; // count the number of vowels found in string text
		} else {
			j = -1;
		}
	}
	if (count == 0){
		return "\""; // empty string
	} else if (count > 2){
		return "\""; // single character
	} else{
		string temp(text);
    sort(begin(temp), end(temp));
		if (temp.size() == 1){
    	string out;
        while (!isalnum(temp[0]))
            out += '*';
        return "\"" + replace_all<std::string, std::back_inserter>(out, 'a', "*") + "\"";
		} else {
        string out;
        for (int i=0,j;i<text.size();++i) // loop over the string `text' again and replace each vowel with an appropriate character
    		if (!isalpha(temp[i])){
            continue;
          } if (isalnum(temp[