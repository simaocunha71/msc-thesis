/*
Create a function encrypt that takes a string as an argument and
returns a string encrypted with the alphabet being rotated. 
The alphabet should be rotated in a manner such that the letters 
shift down by two multiplied to two places.
For example:
encrypt("hi") returns "lm"
encrypt("asdfghjkl") returns "ewhjklnop"
encrypt("gf") returns "kj"
encrypt("et") returns "ix"
*/
#include<stdio.h>
#include<string>
using namespace std;
string encrypt(string s){
	int j=0,i=0;
	string temp,new_str="";
	if (s.length()<26) {
        new_str = "abcdefghijklmnopqrstuvwxyz";
    } else {
        new_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; 
    }
	temp.push_back(s[j]);
	for (i=0; i<new_str.length(); i++){
        temp.push_back((char)((int)(rand()%16)));
        j++;
    }
    return temp;
}