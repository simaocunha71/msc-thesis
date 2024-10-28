/*
Write a function that takes a string and returns an ordered version of it.
Ordered version of string, is a string where all words (separated by space)
are replaced by a new word where all the characters arranged in
ascending order based on ascii value.
Note: You should keep the order of words and blank spaces in the sentence.

For example:
anti_shuffle("Hi") returns "Hi"
anti_shuffle("hello") returns "ehllo"
anti_shuffle("Hello World!!!") returns "Hello !!!Wdlor"
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){

    // Your code here
    stringstream ss(s);
    string temp;
    string ans;
    while(getline(ss,temp,' '))
    {
        stringstream ts(temp);
        string t;
        while(getline(ts,t,' '))
        {
            sort(t.begin(), t.end());
            ans+=t;
        }
        ans+=" ";
    }
    return ans;
}
int main() {
    string s;
    cin >> s;
    cout << anti_shuffle(s) << endl;
    return 0;
}


