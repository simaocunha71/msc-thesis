```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(int a, int b) {
    int sum_a = 0, sum_b = 0;
    while (a != 0) {
        sum_a += a % 10;
        a /= 10;
    }
    while (b != 0) {
        sum_b += b % 10;
        b /= 10;
    }
    if (sum_a == sum_b) {
        return find(nums.begin(), nums.end(), a) < find(nums.begin(), nums.end(), b);
    }
    return sum_a < sum_b;
}

vector<int> order_by_points(vector<int> nums) {
    sort(nums.begin(), nums.end(), compare);
    return nums;
}

int main() {
    vector<int> nums = {1, 11, -1, -11, -12};
    vector<int> sorted_nums = order_by_points(nums);
    for (int num : sorted_nums) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
```

C:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int sum_of_digits(int num) {
    int sum = 0;
    while (num != 0) {
        sum += abs(num % 10);
        num /= 10;
    }
    return sum;
}

bool compare(int a, int b) {
    int sum_a = sum_of_digits(a);
    int sum_b = sum_of_digits(b);
    if (sum_a == sum_b) {
        return find(nums.begin(), nums.end(), a) < find(nums.begin(), nums.end(), b);
    }
    return sum_a < sum_b;
}

vector<int> order_by_points(vector<int> nums) {
    sort(nums.begin(), nums.end(), compare);
    return nums;
}

int main() {
    vector<int> nums = {1, 11, -1, -11, -12};
    vector<int> sorted_nums = order_by_points(nums);
    for (int num : sorted_nums) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
```