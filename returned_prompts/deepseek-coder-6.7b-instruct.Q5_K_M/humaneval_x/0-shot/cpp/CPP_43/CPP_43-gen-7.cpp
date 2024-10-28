    for(int i=0;i<l.size();i++){
        for(int j=i+1;j<l.size();j++){
            if(l[i]+l[j]==0){
                return true;
            }
        }
    }
    return false;
}

int main() {
    vector<int> v1 = {1, 3, 5, 0};
    vector<int> v2 = {1, 3, -2, 1};
    vector<int> v3 = {1, 2, 3, 7};
    vector<int> v4 = {2, 4, -5, 3, 5, 7};
    vector<int> v5 = {1};

    printf("%d\n", pairs_sum_to_zero(v1)); // false
    printf("%d\n", pairs_sum_to_zero(v2)); // false
    printf("%d\n", pairs_sum_to_zero(v3)); // false
    printf("%d\n", pairs_sum_to_zero(v4)); // true
    printf("%d\n", pairs_sum_to_zero(v5)); // false

    return 0;
}

*/

*/

//src/algorithms/search/pairs_sum_to_zero.cpp
#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

bool pairs_sum_to_zero(vector<int> l){
    unordered_set<int> s;
    for(int i=0;i<l.size();i++){
        if(s.find(-l[i]) != s.end()){
            return true;
        }
        s.insert(l[i]);
    }
    return false;
}

int main() {
    vector<int> v1 = {1, 3, 5, 0};
    vector<int> v2 = {1, 3, -2, 1};
    vector<int> v3 = {1, 2, 3, 7