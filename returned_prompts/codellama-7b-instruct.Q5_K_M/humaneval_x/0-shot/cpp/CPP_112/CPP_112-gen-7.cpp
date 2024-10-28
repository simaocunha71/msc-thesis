/*
Task
We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
then check if the result string is palindrome.
A string is called palindrome if it reads the same backward as forward.
You should return a vector containing the result string and "True"/"False" for the check.
Example
For s = "abcde", c = "ae", the result should be ("bcd","False")
For s = "abcdef", c = "b"  the result should be ("acdef","False")
For s = "abcdedcba", c = "ab", the result should be ("cdedc","True")
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> reverse_delete(string s,string c){

// Complete this function

vector<string> result;

string new_s = s;

for(int i = 0; i<c.length();i++){

for(int j = 0; j<s.length(); j++){

if(new_s[j] == c[i]){

new_s.erase(new_s.begin()+j);

j--;

}

}

}

string new_s_rev = new_s;

reverse(new_s_rev.begin(), new_s_rev.end());

if(new_s == new_s_rev){

result.push_back(new_s);

result.push_back("True");

}else{

result.push_back(new_s);

result.push_back("False");

}

return result;

}

int main(){

string s = "abcdedcba";

string c = "ab";

vector<string> result = reverse_delete(s,c);

cout << result[0] << endl;

cout << result[1] << endl;

return 0;

}

