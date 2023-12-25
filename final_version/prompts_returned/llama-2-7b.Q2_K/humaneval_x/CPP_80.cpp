/*
You are given a string s.
Your task is to check if the string is happy or not.
A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
For example:
is_happy("a") => false
is_happy("aa") => false
is_happy("abcd") => true
is_happy("aabb") => false
is_happy("adb") => true
is_happy("xyy") => false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool is_happy(string s){
	int counter=0,counter1=0,counter2=0;  //initializing the counters for the consonants and vowels, and to count the number of "a"s in the string
    int i=0;
	for(i=0;i<s.size();++i) {//incrementing the counter for every character in the string
	if(counter==1 || counter2==1){
		if(!(is_happy("aa"))) break;  //check if this is happy or not, break and go back to the beginning of the loop otherwise
	} else {
		if(s[i]!='a'){counter++;}else counter2++;}//increment counters for all the characters except "a", increment the counter1 by 1 only if 'a' appears after a non-vowel character, increment counter2 by one only if there are more than two consecutive 'a's without any other distinct vowels.
	} //checking and reinitating the counters for the third time
	if(!(counter==3 && counter1==0 && counter2==0) ){
		return false;//not happy, as there isn't a 3 consecutive sequence of characters without the same character appearing twice in a row.
    } else {return true;} //happy if and only if all three conditions are satisfied.
}
int main(){
	string s="";
	while(gets(&s)!=EOF){//accepting input till EOF, printing it to the screen then
	if(!is_happy(s)){printf("NOT HAPPY!!\n");}