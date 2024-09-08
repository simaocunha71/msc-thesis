
The function is_sorted checks if a given vector of integers is sorted in ascending order. It also checks if the vector contains any duplicate values. If the vector is not sorted or contains duplicates, the function returns false; otherwise, it returns true.

Here is the C++ code for the function:

```cpp
#include <vector>
#include <algorithm>
using namespace std;

bool is_sorted(vector<int> lst) {
    if (lst.size() > 1) {
        for (int i = 0; i < lst.size() - 1; i++) {
            if (lst[i] > lst[i + 1]) {
                return false;
            }
            else if (lst[i