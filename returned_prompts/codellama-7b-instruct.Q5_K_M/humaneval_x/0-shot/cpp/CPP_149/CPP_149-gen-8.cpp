/*
Write a function that accepts a vector of strings as a parameter,
deletes the strings that have odd lengths from it,
and returns the resulted vector with a sorted order,
The vector is always a vector of strings and never a vector of numbers,
and it may contain duplicates.
The order of the vector should be ascending by length of each word, and you
should return the vector sorted by that rule.
If two words have the same length, sort the vector alphabetically.
The function should return a vector of strings in sorted order.
You may assume that all words will have the same length.
For example:
assert vector_sort({"aa", "a", "aaa"}) => {"aa"}
assert vector_sort({"ab", "a", "aaa", "cd"}) => {"ab", "cd"}
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> sorted_list_sum(vector<string> lst){
    vector<string> result;
    for(int i=0;i<lst.size();i++){
        if(lst[i].length()%2==0){
            result.push_back(lst[i]);
        }
    }
    sort(result.begin(), result.end(), sort_str());
    return result;
}
int main(){
    vector<string> lst={"ab","aaa","a","c"};
    vector<string> result=sorted_list_sum(lst);
    for(int i=0;i<result.size();i++){
        cout<<result[i]<<endl;
    }
    return 0;
}

