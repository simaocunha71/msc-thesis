```cpp
#include <vector>
#include <algorithm>
using namespace std;

vector<int> sort_third(vector<int> l){
    vector<int> third_indices;
    for (int i = 2; i < l.size(); i += 3) {
        third_indices.push_back(l[i]);
    }
    sort(third_indices.begin(), third_indices.end());
    int j = 0;
    for (int i = 2; i < l.size(); i += 3) {
        l[i] = third_indices[j++];
    }
    return l;
}
```
