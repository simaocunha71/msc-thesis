    int distinct_characters = 0;
    vector<char> v;
    for(int i = 0; i < str.size(); i++) {
        if(find(v.begin(), v.end(), str[i]) == v.end()) {
            v.push_back(str[i]);
            distinct_characters++;
        }
    }
    return distinct_characters;
}





/*
Given an array of integers, find out if there are two integers such that one of them is a multiple of the other.
>>> multiple_integers([4, 6, 8, 9, 10])
True
>>> multiple_integers([2, 3, 5, 7, 8])
False
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
bool multiple_integers(vector<int> arr) {
    int n = arr.size();
    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {
            if(arr[i] % arr[j] == 0 || arr[j] % arr[i] == 0) {
                return true;
            }
        }
    }
    return false;
}





/*
Given an array of integers, find out the index of the first occurrence of an element in the array. If the element does not exist in the array, return -1.
>>> first_occurrence_index([1, 2, 3, 4, 5], 3)
2
>>> first_occurrence_index([1, 2, 3, 4, 5], 6)
-1
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int first_occurrence_index(vector<int> arr, int element) {
    int n = arr.size();
    for(int i = 0; i < n; i++) {
        if(arr[i] == element) {
           