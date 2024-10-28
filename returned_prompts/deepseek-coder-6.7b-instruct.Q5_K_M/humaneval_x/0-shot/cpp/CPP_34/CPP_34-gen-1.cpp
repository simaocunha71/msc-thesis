    sort(l.begin(), l.end());
    l.erase(unique(l.begin(), l.end()), l.end());
    return l;
}

int main(){
    vector<int> v{5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> u = unique(v);
    for(int i=0; i<u.size(); i++)
        printf("%d ", u[i]);
    return 0;
}

Output:
0 2 3 5 9 123

Explanation:
The function unique() is a standard algorithm in C++ STL which rearranges the elements in the range [first, last) such that all elements with equivalent values are grouped together. It also returns a pointer to the new logical end of the range.
The function sort() is used to sort the elements in ascending order.
Then, the function erase() is used to remove the duplicate elements from the vector. The erase() function takes two arguments, the first is the iterator pointing to the first element to be deleted and the second is the iterator pointing to the position after the last element to be deleted.
In the main function, we call the function unique() and print out the unique elements in the vector.
*/


A: The problem is that you are trying to return a vector of int while the unique function is designed to work with iterators. You can use std::set instead.
std::set is a container that stores unique elements following a specific order. The key feature of a set is that all elements in a set are unique and all elements in a set are always in a sorted order.
#include <iostream>
#include <set>
#include <vector>
using namespace std;

set<int> unique(vector<int> l) {
    set<int> s(l.begin(), l.end());
    return s;
}

int main() {
    vector<int> v{5, 3, 5, 2, 3, 3, 9, 0, 123};
    set<int> u = unique(v);
    for (auto it