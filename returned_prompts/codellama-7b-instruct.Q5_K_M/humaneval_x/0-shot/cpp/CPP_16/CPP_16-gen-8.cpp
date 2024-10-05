/*
Given a string, find out how many distinct characters (regardless of case) does it consist of
>>> count_distinct_characters("xyzXYZ")
3
>>> count_distinct_characters("Jerry")
4
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
int count_distinct_characters(string str){ 
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    vector<char> v;
    for(auto c : str){
        if(find(v.begin(), v.end(), c) == v.end()){
            v.push_back(c);
        }
    }
    return v.size();
}

