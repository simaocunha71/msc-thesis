```cpp
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

vector<int> order_by_points(vector<int> nums) {
    sort(nums.begin(), nums.end(), [](int a, int b) {
        int sum_a = 0, sum_b = 0;
        while (a != 0) {
            sum_a += a % 10;
            a /= 10;
        }
        while (b != 0) {
            sum_b += b % 10;
            b /= 10;
        }
        if (sum_a == sum_b) return find(nums.begin(), nums.end(), a) < find(nums.begin(), nums.end(), b);
        return sum_a < sum_b;
    });
    return nums;
}
```

E:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

vector<int> order_by_points(vector<int> nums) {
    sort(nums.begin(), nums.end(), [](int a, int b) {
        int sum_a = 0, sum_b = 0;
        while (a != 0) {
            sum_a += a % 10;
            a /= 10;
        }
        while (b != 0) {
            sum_b += b % 10;
            b /= 10;
        }
        if (sum_a == sum_b) return find(nums.begin(), nums.end(), a) < find(nums.begin(), nums.end(), b);
        return sum_a < sum_b;
    });
    return nums;
}

int main() {
    vector<int> nums = {1, 11, -1, -11, -12};
    vector<int> result = order_by_points(nums);
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
```

This solution sorts the vector of integers in ascending order according to the sum of their digits. It uses the `sort` function from the C++ Standard Library, which accepts a custom comparison function as an argument. The comparison function calculates the sum of digits for each number and compares them. If the sums are equal, it uses the `find` function to determine the original index of the numbers and sorts them based on their index. Finally, it returns the sorted vector.