/*Write a function that returns true if all numbers in the vector l are below threshold t.
>>> below_threshold({1, 2, 4, 10}, 100)
true
>>> below_threshold({1, 20, 4, 10}, 5)
false
*/

#include<vector>
#include<iostream>
using namespace std;
bool below_threshold(vector<int> l, int t){
    return all_of(l.begin(), l.end(), [t](int i) { return i < t; });
}

int main(){
    vector<int> l1 = {1, 2, 4, 10};
    vector<int> l2 = {1, 20, 4, 10};
    cout << below_threshold(l1, 100) << endl; // true
    cout << below_threshold(l2, 5) << endl; // false
    return 0;
}

