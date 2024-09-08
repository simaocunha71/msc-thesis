    // Sort both lists
    sort(l1.begin(), l1.end());
    sort(l2.begin(), l2.end());

    // Initialize two pointers
    int i = 0, j = 0;

    // Traverse both lists
    vector<int> commonElements;
    while (i < l1.size() && j < l2.size()) {
        if (l1[i] < l2[j])
            i++;
        else if (l2[j] < l1[i])
            j++;
        else {
            commonElements.push_back(l1[i]);
            i++;
            j++;
        }
    }

    // Remove duplicates and sort
    sort(commonElements.begin(), commonElements.end());
    commonElements.erase(unique(commonElements.begin(), commonElements.end()), commonElements.end());

    return commonElements;
}

int main() {
    vector<int> l1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> l2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> common;
    common = common(l1,l2);
    for (int i = 0; i < common.size(); i++) {
        printf("%d ", common[i]);
    }
    return 0;
}

B:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> common(vector<int>& l1, vector<int>& l2) {
    vector<int> commonElements;

    // Convert the vectors to sets for efficient operations
    set<int> set1(l1.begin(), l1.end());
    set<int> set2(l2.begin(), l2.end());

    // Find the intersection of the two sets
    set<int> intersection(set1.begin(), set1.end());
    set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(),
                     std::inserter(intersection, intersection.end()));

    // Copy the intersection to a vector
    for (auto& element : intersection) {
        commonElements.push_back(element);
    }

    return commonElements;
}

int main() {
    vector<int> l1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> l2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> common;
