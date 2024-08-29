#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string longest(vector<string> strings){
    string longest = "";
    for(string s : strings){
        if(s.length() > longest.length()){
            longest = s;
        }
    }
    return longest;
}