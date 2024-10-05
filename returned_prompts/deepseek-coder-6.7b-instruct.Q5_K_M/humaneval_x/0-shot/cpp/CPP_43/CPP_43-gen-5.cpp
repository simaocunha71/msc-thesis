    unordered_set<int> set;
    for (int num : l) {
        if (set.find(-num) != set.end()) {
            return true;
        }
        set.insert(num);
    }
    return false;
}

This solution uses an unordered_set to store the elements of the vector. It iterates through the vector and for each element, it checks if its negation is in the set. If it is, it means there are two elements in the vector that sum to zero, so it returns true. If it doesn't find a pair, it adds the current element to the set and continues. If it finishes the loop without finding a pair, it returns false.

The complexity of this solution is O(n), because it iterates through the vector once. It scales well for large vectors.

*/

#include<iostream>
#include<unordered_set>
#include<vector>
using namespace std;

bool pairs_sum_to_zero(vector<int> l){
    unordered_set<int> set;
    for (int num : l) {
        if (set.find(-num) != set.end()) {
            return true;
        }
        set.insert(num);
    }
    return false;
}

int main()
{
    vector<int> l = {2, 4, -5,