    vector<int> v;

B:
    sort(l1.begin(), l1.end());
    sort(l2.begin(), l2.end());

C:
    set_intersection(l1.begin(), l1.end(), l2.begin(), l2.end(), back_inserter(v));

D:
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());

E:
    return v;
}

*/

int main() {
    vector<int> l1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> l2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> result = common(l1, l2);
    for(int i=0; i<result.size(); i++)
        printf("%d ", result[i]);
    return 0;
}

*/

/*
The code sorts the vectors, then uses the set_intersection method to find the common elements. The common elements are then sorted and duplicates are removed.
*/

//code by Rahul Kumar
//rahulkcs09@gmail.com

//C++ program to find the common elements in two vectors
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> common(vector<int> &l1, vector<int> &l2) {
    vector<int> v;
    sort(l1.begin(), l1.end());
    sort(l2.begin(), l2.end());
    set_intersection(l1.begin(), l1.end(), l2.begin(), l2.end(), back_inserter(v));
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    return v;
}

int main() {
    vector<int> l1 = {1, 4