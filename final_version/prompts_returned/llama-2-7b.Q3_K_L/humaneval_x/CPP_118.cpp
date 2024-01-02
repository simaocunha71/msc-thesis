/*
You are given a word. Your task is to find the closest vowel that stands between 
two consonants from the right side of the word (case sensitive).

Vowels in the beginning and ending doesn't count. Return empty string if you didn't
find any vowel met the above condition. 

You may assume that the given string contains English letter only.

Example:
get_closest_vowel("yogurt") ==> "u"
get_closest_vowel("FULL") ==> "U"
get_closest_vowel("quick") ==> ""
get_closest_vowel("ab") ==> ""
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string get_closest_vowel(string word){
	int pos=0, vowels_count=1, char_pos=-1;
	if(word[0]=='a'||word[0]=='A'){
		char_pos = 0;
	}
	for(int i=0;i< word.length();i++){
		if((word[i]>='a'&&word[i]<='z')||(word[i]>= 'A'&& word[i]<= 'Z')){
			pos = i;
		} else {
			vowels_count++;
		}
		if((char_pos==-1)&&word[i] == 'a'){
			char_pos=i;
		}
	}
	int pos2 = 0, vowels_count2=1, char_pos3=-1;
	for(int i=0;i< word.length();i++){
		if((word[i]>='a'&&word[i]<='z')||(word[i]>= 'A'&& word[i]<= 'Z')){
			pos2 = i;
		} else {
			vowels_count2++;
		}
		if((char_pos3==-1)&&word[i] == 'a'){
			