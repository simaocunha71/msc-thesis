    int count=0;
    for(int i=0;i<lst[0].length();i++){
        if(lst[0][i]==')')
            count--;
        else
            count++;
        if(count<0)
            return "No";
    }
    count=0;
    for(int i=0;i<lst[1].length();i++){
        if(lst[1][i]=='(')
            count--;
        else
            count++;
        if(count<0)
            return "No";
    }
    return "Yes";
}




/*
Given a string of lowercase alphanumeric characters, return the number of
different characters in the string. If the string is empty, then return 0.

Examples:
different_chars("") == 0
different_chars("a") == 1
different_chars("aa") == 1
different_chars("abc") == 3

*/

#include<stdio.h>
#include<set>
#include<string>
using namespace std;
int different_chars(string s){
    set<char> c;
    for(int i=0;i<s.length();i++)
        c.insert(s[i]);
    return c.size();
}


/*
A "good" string is a string that can be arranged to form a valid parentheses
string (i.e. every open parenthesis '(' is matched with a close parenthesis ')').
A "bad" string is a string that cannot be arranged to form a valid parentheses
string. For example, "()()" is a good string, while "))(()" is a bad string.
Write a function that takes a string of lowercase alphanumeric characters and
returns true if the string is a good one, and false if it is not.

Examples:
is_good("()()") == true
is_good("))(()") == false
is_good("") == true

*/
#include<stdio.h>
#include<stack>
#include<string>
using namespace std;
bool is_good(string s){
   