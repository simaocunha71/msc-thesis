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
	vector<string> words;
	string word;
	int i=0;
	while(s[i]!='\0'){
		if(s[i]==' '){
			word[i]=s[i];
			i++;
		}
		else{
			while(s[i]!=' '){
				word[i]=s[i];
				i++;
			}
			words.push_back(word);
			word="";
			i++;
		}
	}
	return words;
}

