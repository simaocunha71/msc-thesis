/*
You will be given a string of words separated by commas or spaces. Your task is
to split the string into words and return a vector of the words.

For example:
words_string("Hi, my name is John") == {"Hi", "my", "name", "is", "John"}
words_string("One, two, three, four, five, six") == {"One", 'two", 'three", "four", "five", 'six"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> words_string(string s){
	int length = s.length();
	vector<string> string_return(length);
	for ( int i=0;i<s.length()-1;i++) {
		if(s[i]==','){
			string_return[i+1]=string_return[i];
		} else {
			string_return[i]+=", ";
		}
	}
	string_return.back()=s;
	return string_return;
}
int main(void) {
    // Your code goes here...
    
    return 0;
}