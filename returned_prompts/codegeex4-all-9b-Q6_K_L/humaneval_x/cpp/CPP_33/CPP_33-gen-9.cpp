```cpp
#include <vector>
#include <algorithm>

using namespace std;

vector<int> sort_third(vector<int> l) {
    vector<int> thirdIndices;
    for (int i = 2; i < l.size(); i += 3) {
        thirdIndices.push_back(l[i]);
    }
    sort(thirdIndices.begin(), thirdIndices.end());
    int index = 0;
    for (int i = 2; i < l.size(); i += 3) {
        l[i] = thirdIndices[index++];
    }
    return l;
}
```
