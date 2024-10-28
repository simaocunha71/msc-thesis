     vector<int> ans;
     int min_even = 10001, min_index = -1;
     for(int i = 0; i < arr.size(); i++){
         if(arr[i] % 2 == 0 && arr[i] < min_even){
             min_even = arr[i];
             min_index = i;
         }
     }
     if(min_index != -1){
         ans.push_back(min_even);
         ans.push_back(min_index);
     }
     return ans;
}



int main(){
    vector<int> arr = {4,2,3};
    vector<int> res = pluck(arr);
    for(int i=0; i<res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}




Output: 2 1
Explanation: 2 has the smallest even value, and 2 has the smallest index.
*/

//src/main.cpp
#include <iostream>
#include <vector>
#include "solution.h"
using namespace std;

int main() {
    vector<int> arr = {4,2,3};
    vector<int> res = pluck(arr);
    for(int i=0; i<res.size(); i++)
        cout << res[i] << " ";
    return 0;
}

//src/solution.cpp
#include "solution.h"
#include <vector>
using namespace std;

vector<int> pluck(vector<int> arr){
    vector<int> ans;
    int min_even = 10001, min_index = -1;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0 && arr[i] < min_even){
            min_even = arr[i];
            min_index = i;
        }
    }
    if(min_index != -1){
        ans.push_back