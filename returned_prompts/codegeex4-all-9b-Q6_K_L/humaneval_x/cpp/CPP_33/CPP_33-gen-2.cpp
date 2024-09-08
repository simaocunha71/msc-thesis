```cpp
#include <vector>
#include <algorithm>
using namespace std;

vector<int> sort_third(vector<int> l) {
    vector<int> divisible_by_three_indices;
    for (int i = 0; i < l.size(); i += 3) {
        divisible_by_three_indices.push_back(l[i]);
    }
    sort(divisible_by_three_indices.begin(), divisible_by_three_indices.end());

    int index = 0;
    for (int i = 0; i < l.size(); i += 3) {
        l[i] = divisible_by_three_indices[index++];
    }
    return l;
}
```
