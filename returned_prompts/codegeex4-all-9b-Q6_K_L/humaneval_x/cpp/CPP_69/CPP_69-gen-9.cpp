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
#include <vector>
#include <unordered_map>
using namespace std;
int search(vector<int> lst){
    unordered_map<int, int> freq;
    for(int i = 0; i < lst.size(); i++){
        freq[lst[i]]++;
    }
    int max = -1;
    for(auto it = freq.begin(); it != freq.end(); it++){
        if(it->second >= it->first && it->first > max){
            max = it->first;
        }
    }
    return max;
}