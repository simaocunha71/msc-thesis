/*
You are given a non-empty vector of positive integers. Return the greatest integer that is greater than 
zero, and has a frequency greater than or equal to the value of the integer itself. 
The frequency of an integer is the number of times it appears in the vector.
If no such a value exist, return -1.
Examples:
    search({4, 1, 2, 2, 3, 1}) == 2
    search({1, 2, 2, 3, 3, 3, 4, 4, 4}) == 3
    search({5, 5, 4, 4, 4}) == -1
*/
#include<stdio.h>
#include<vector>
#include<map>
using namespace std;
int search(vector<int> lst){
    map<int,int> mp;
    for(int i=0;i<lst.size();i++){
        mp[lst[i]]++;
    }
    int ans=-1;
    for(int i=0;i<lst.size();i++){
        if(mp[lst[i]]>=lst[i]){
            ans=max(ans,lst[i]);
        }
    }
    return ans;

B:
/*
You are given a non-empty vector of positive integers. Return the greatest integer that is greater than 
zero, and has a frequency greater than or equal to the value of the integer itself. 
The frequency of an integer is the number of times it appears in the vector.
If no such a value exist, return -1.
Examples:
    search({4, 1, 2, 2, 3, 1}) == 2
    search({1, 2, 2, 3, 3, 3, 4, 4, 4}) == 3
    search({5, 5, 4, 4, 4}) == -1
*/
#include<stdio.h>
#include<vector>
#include<map>
using namespace std;
int search(vector<int> lst){
    map<int,int> mp;
    for(int i=0;i<lst.size();i++){
        mp[lst[i]]++;
    }
    int ans=-1;
    for(int i=0;i<lst.size();i++){
        if(mp[lst[i]]>=lst[i]){
            ans=max(ans,lst[i]);
        }
    }
    return ans;
}