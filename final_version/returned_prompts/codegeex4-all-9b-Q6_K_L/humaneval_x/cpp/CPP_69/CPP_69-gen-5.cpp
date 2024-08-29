/*
The key to the problem is to find the greatest integer that has a frequency greater than or equal to its value. 
We can achieve this by using a map to store the frequency of each integer. 
Then, we iterate through the map and find the greatest integer that satisfies the condition. 
If no such integer exists, we return -1. 
The time complexity of this solution is O(n), where n is the size of the input vector.
*/
#include<stdio.h>
#include<vector>
using namespace std;
#include<map>
int search(vector<int> lst){
    map<int, int> freq;
    for(int i=0; i<lst.size(); i++){
        freq[lst[i]]++;
    }
    int ans=-1;
    for(auto it=freq.begin(); it!=freq.end(); it++){
        if(it->second >= it->first){
            ans = max(ans, it->first);
        }
    }
    return ans;
}