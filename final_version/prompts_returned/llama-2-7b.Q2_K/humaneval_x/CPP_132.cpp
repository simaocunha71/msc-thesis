/*
Create a function that takes a string as input which contains only square brackets.
The function should return true if and only if there is a valid subsequence of brackets
where at least one bracket in the subsequence is nested.

is_nested("[[]]") ➞ true
is_nested("[]]]]]]][[[[[]") ➞ false
is_nested("[][]") ➞ false
is_nested("[]") ➞ false
is_nested("[[][]]") ➞ true
is_nested("[[]][[") ➞ true
*/
#include<stdio.h>
#include<string>
using namespace std;
bool is_nested(string str){
	int counter = 0, bracket = 0, nestedness = 0;
	for(int i=0 ; i < str.length(); ++i) {
		if(str[i] == '['){
			bracket++;
		}else if (str[i] == ']'){
			counter--; nestedness = bracket - counter;
		}else if (nestedness >= 0) { // If we have a nested subsequence, then we exit here
			return true;
		}
	}
	if(bracket == 1){// The first [ is the start of an invalid sequence
		counter = 0; nestedness = -1; return false;
	}else if (nestedness >= 0) { // Brackets exist in a valid sequence
		return true;
	}
	return false;
}
// Main()
int main(){
    int i,j=0;
    string s = "[][[]]";//s is being considered as string.
    cout <<"enter any one digit no: ";cin >>i;
    printf("Entered no is %d",i);
	if(is_nested(s)) {
		for (int k=0;k<s.length();k++) {
        	printf("%c",s[k]);} //printing the string s in the format of numbers
    }else{//if no is not valid then print 'no' is invalid