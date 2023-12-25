/*
Input to this function is a string representing musical notes in a special ASCII format.
Your task is to parse this string and return vector of integers corresponding to how many beats does each
not last.

Here is a legend:
"o" - whole note, lasts four beats
"o|" - half note, lasts two beats
".|" - quater note, lasts one beat

>>> parse_music("o o| .| o| o| .| .| .| .| o o")
{4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> parse_music(string music_string){ 
	int i=0,j=0,beats=0;   
	for (i = 4; i >= 2; i--) {   //starting from the last character in the string
		if ((music_string[i] == '.') && (music_string[i-1] != 'o')){   //check if it is a dot and then check next char as to whether it is o or not
		beats=0;   
	}else if(((music_string[i]=='o')||(music_string[i-1]=="o"))&& (music_string[i]!='|')){   //check if the char is 'o' and then check next as to whether it is a | or not
	j++; beats=j; 
	}else if(((music_string[i]=='o')||(music_string[i-1]=="o")) && (music_string[i+1]!='|')){   //check if the char is 'o' and then check next as to whether it is a | or not
	j++; beats=beats+2;   }else{  j++; 
	if ((i != music_string.length() -2) && (music_string[++i] == '.')&&(music_string[++i-1]!='|')){      //check if the