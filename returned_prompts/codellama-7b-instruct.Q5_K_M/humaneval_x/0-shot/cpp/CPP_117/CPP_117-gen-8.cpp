/*
Given a string s and a natural number n, you have been tasked to implement 
a function that returns a vector of all words from string s that contain exactly 
n consonants, in order these words appear in the string s.
If the string s is empty then the function should return an empty vector.
Note: you may assume the input string contains only letters and spaces.
Examples:
select_words("Mary had a little lamb", 4) ==> {"little"}
select_words("Mary had a little lamb", 3) ==> {"Mary", "lamb"}
select_words('simple white space", 2) ==> {}
select_words("Hello world", 4) ==> {"world"}
select_words("Uncle sam", 3) ==> {"Uncle"}
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){
	vector<string> v;
	stringstream ss(s);
	string word;
	while(ss>>word){
		int consonants=0;
		for(char c : word){
			if(!isalpha(c)) continue;
			if(isupper(c) || islower(c)) {
				if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u') continue;
				consonants++;
			}
		}
		if(consonants==n) v.push_back(word);
	}
	return v;
}

