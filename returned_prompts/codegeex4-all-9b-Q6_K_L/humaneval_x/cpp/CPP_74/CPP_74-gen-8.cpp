/*
Write a function that accepts two vectors of strings and returns the vector that has 
total number of chars in the all strings of the vector less than the other vector.

if the two vectors have the same number of chars, return the first vector.

Examples
total_match({}, {}) ➞ {}
total_match({"hi", "admin"}, {"hI", "Hi"}) ➞ {"hI", "Hi"}
total_match({"hi", "admin"}, {"hi", "hi", "admin", "project"}) ➞ {"hi", "admin"}
total_match({"hi", "admin"}, {"hI", "hi", "hi"}) ➞ {"hI", "hi", "hi"}
total_match({"4"}, {"1", "2", "3", "4", "5"}) ➞ {"4"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> total_match(vector<string> lst1,vector<string> lst2){

    int s1=0,s2=0;
    for(int i=0;i<lst1.size();i++){
        s1+=lst1[i].length();
    }
    for(int i=0;i<lst2.size();i++){
        s2+=lst2[i].length();
    }
    if(s1<s2) return lst1;
    if(s1>s2) return lst2;
    return lst1;
}

B:
/*
Write a function that accepts two vectors of strings and returns the vector that has 
total number of chars in the all strings of the vector less than the other vector.

if the two vectors have the same number of chars, return the first vector.

Examples
total_match({}, {}) ➞ {}
total_match({"hi", "admin"}, {"hI", "Hi"}) ➞ {"hI", "Hi"}
total_match({"hi", "admin"}, {"hi", "hi", "admin", "project"}) ➞ {"hi", "admin"}
total_match({"hi", "admin"}, {"hI", "hi", "hi"}) ➞ {"hI", "hi", "hi"}
total_match({"4"}, {"1", "2", "3", "4", "5"}) ➞ {"4"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> total_match(vector<string> lst1,vector<string> lst2){

    int s1=0,s2=0;
    for(int i=0;i<lst1.size();i++){