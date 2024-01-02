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
	if(s==NULL || s[0]=='\0')return vector<string>();
	int i=0,pos=0;
    for (auto it = begin(s); it != end(s); ++it) {
        if(*it == ' ') {
            pos++;
            continue;
        } 
        
        i+=1;
        if(i==n) return vector<string>();
        
    }
    
    int j=pos+1,k=0;
	int count=0;
	vector<string> vec;
	while(j<s.length()){
        if((*s)[j] == ' ') {
            pos++;
            continue;
        } 
        
    	int temp=pos-count+1;
    	if(temp>=j)k++;
    	else j+=k;
    	if(!vec.empty())break;
    	vec.push_back(string(s+temp,i));
    	k=0;
    	pos++;
        if(j<s.length()){
            
            if((*s)[j] == ' ') {
                pos++;
                continue;
            } 
        
        }