    for(int i=0; i < l.size(); i++){
        for(int j=i+1; j<l.size(); j++){
            if(l[i] + l[j] == 0){
                return true;
            }
        }
    }
    return false;
}

int main() {
    vector<int> l1 = {1, 3, 5, 0};
    vector<int> l2 = {1, 3, -2, 1};
    vector<int> l3 = {1, 2, 3, 7};
    vector<int> l4 = {2, 4, -5, 3, 5, 7};
    vector<int> l5 = {1};
    printf("%d\n", pairs_sum_to_zero(l1)); // false
    printf("%d\n", pairs_sum_to_zero(l2)); // false
    printf("%d\n", pairs_sum_to_zero(l3)); // false
    printf("%d\n", pairs_sum_to_zero(l4)); // true
    printf("%d\n", pairs_sum_to_zero(l5)); // false
    return 0;
}


A: This program could be optimized by using a set or unordered_set data structure instead of the vector, because checking for the existence of an element in a set or unordered_set is faster than checking for the existence of an element in a vector. 

Here is the optimized version of the program using set:
```cpp
#include<iostream>
#include<set>
#include<vector>
using namespace std;

bool pairs_sum_to_zero(vector<int> l){
    set<int> s;
    for (int i = 0; i < l.size(); i++) {
        if (s.find(-l[i]) != s.end()) {
            return true;
        }
        s.insert(l[i]);
    }
    return false;
}

int main() {
    vector<int> l1 = {1, 3, 5, 0};
