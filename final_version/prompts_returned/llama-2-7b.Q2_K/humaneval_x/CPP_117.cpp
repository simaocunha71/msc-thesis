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
    vector<string> res;
    int j=0,k,c;
    while(j<=n-1){
        c=(s[j])%26;
        k=(s[j+1])%26;
        if(c==k||c!=0||c==25&&k!=25) res.push_back(s);
        else j=j+2;
    }
    return res;
}
int main()
{
    string s="Mary had a little lamb";
    int n=4;
    cout<<select_words(s,n)<<endl;
    return 0;
}