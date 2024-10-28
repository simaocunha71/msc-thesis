

/*

B:

Task
You are given a string of alphanumeric characters. You have to check if all the alphanumeric characters are in uppercase.
Then you have to delete all the spaces and underscores from the string and check if the result is a palindrome.
You should return "True"/"False" for the check.

Example:
For s = "A_B_C_", the result should be "True"
For s = "A_B_Z_", the result should be "False"
For s = "A_B_C__", the result should be "True"

*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string delete_space_under(string s){
    for(int i = 0; i < s.size(); i++) {
        if(s[i] == '_' || s[i] == ' '){
            s.erase(i,1);
            i--;
        }
    }
    return s;
}
bool is_palindrome(string s){
    int l = 0;
    int r = s.size() - 1;
    while(l < r){
        if(s[l