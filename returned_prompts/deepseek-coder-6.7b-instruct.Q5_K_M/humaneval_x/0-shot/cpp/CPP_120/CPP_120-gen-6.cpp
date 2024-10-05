    vector<int> ans;
B:
    if(k==0)
        return ans;
C:
    int max_val = *max_element(arr.begin(),arr.end());
    ans.push_back(max_val);
    arr.erase(remove(arr.begin(),arr.end(),max_val),arr.end());
D:
    return maximum(arr,k-1);
}

int main(){
    vector<int> arr = {4, -4, 4};
    int k = 2;
    vector<int> ans = maximum(arr,k);
    for(int i=0;i<ans.size();i++)
        printf("%d ",ans[i]);
    return 0;
}

The provided program uses recursive function to find the maximum k elements from the array and return a sorted vector of those maximum elements.
The maximum element is found using the max_element function from the algorithm library and removed from the array using the erase and remove functions from the algorithm library. 
The removed element is then pushed in the answer vector and the function is called recursively with k decremented by 1.
This process continues until k becomes 0.
The answer vector is returned as the final result.

*/

#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> maximum(vector<int> arr, int k) {
    vector<int> ans;
    if(k==0)
        return ans;
    for(int i=0; i<k; i++) {
        int max_val = *max_element(arr.begin(), arr.end());
        ans.push_back(max_val);
        arr.erase(remove(arr.begin(), arr.end(), max_val), arr.end());
    }
    return ans;
}

int main() {
    vector<int> arr = {4, -4, 4};
    int k = 2;
    vector<int> ans = maximum(arr, k);
    for(int i=0; i<ans.size(); i++)