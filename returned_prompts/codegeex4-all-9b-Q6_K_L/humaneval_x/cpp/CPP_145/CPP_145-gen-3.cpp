```cpp
#include <algorithm>
#include <vector>
using namespace std;

vector<int> order_by_points(vector<int> nums) {
    vector<pair<int, int>> v;
    for (int i = 0; i < nums.size(); i++) {
        int sum = 0;
        int n = abs(nums[i]);
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        v.push_back(make_pair(sum, i));
    }
    sort(v.begin(), v.end());
    vector<int> result;
    for (int i = 0; i < nums.size(); i++) {
        result.push_back(nums[v[i].second]);
    }
    return result;
}
```

C:
```cpp
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

vector<int> order_by_points(vector<int> nums) {
    vector<pair<int, int>> v;
    for (int i = 0; i < nums.size(); i++) {
        int sum = 0;
        int n = abs(nums[i]);
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        v.push_back(make_pair(sum, i));
    }
    sort(v.begin(), v.end());
    vector<int> result;
    for (int i = 0; i < nums.size(); i++) {
        result.push_back(nums[v[i].second]);
    }
    return result;
}
```