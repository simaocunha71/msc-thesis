    int n = lst.size();
    int res = 0;
    for(int i = 0; i < n; i += 2){
        res += lst[i];
    }
    return res;
}

int main(){
    vector<int> lst = {4, 2, 6, 7};
    printf("%d\n", add(lst));
    return 0;
}


*/



/*
Given an array of strings, return the length of the longest one.

Examples:
    longest({"cat", "dog", "moon"}) ==> 3
    longest({"apple", "banana", "carrot"}) ==> 7
    longest({"", "banana", "carrot"}) ==> 7
    longest({"cat", "", "moon"}) ==> 3
*/
#include<string>
#include<vector>
#include<algorithm>
#include<iostream>
using namespace std;
int longest(vector<string> lst){
    int max = 0;
    for(string s : lst){
        int len = s.size();
        if(len > max) max = len;
    }
    return max;
}

int main(){
    vector<string> lst = {"cat", "dog", "moon"};
    cout << longest(lst) << endl;
    return 0;
}



/*
Given a string of lowercase letters, return the length of the longest contiguous substring with all the same letter.

Examples:
    longest({"cat", "dog", "moon"}) ==> 3
    longest({"apple", "banana", "carrot"}) ==> 6
    longest({"", "banana", "carrot"}) ==> 1
    longest({"cat", "", "moon"}) ==> 3
*/
#include<string>
#include<vector>
#include<iostream>
using namespace std;
int longest(string s){
    int max = 0;
    for(int i = 0; i < s.size(); i++) {
        int len = 