    sort(nums.begin(), nums.end(), 
    [](int a, int b) {
        if (abs(accumulate(cbegin(b), cend(b), 0), 0, 0) == 
            abs(accumulate(cbegin(a), cend(a), 0), 0, 0)) {
            return distance(cbegin(nums), cbegin(nums)+find(cbegin(nums), cend(nums), a)) <
                distance(cbegin(nums), cbegin(nums)+find(cbegin(nums), cend(nums), b));
        } else {
            return abs(accumulate(cbegin(b), cend(b), 0), 0, 0) <
                abs(accumulate(cbegin(a), cend(a), 0), 0, 0);
        }
    });
    return nums;
} 
// or
#include<numeric>
#include<algorithm>
using namespace std;
vector<int> order_by_points(vector<int> nums){
    sort(nums.begin(), nums.end(), 
    [&nums](int a, int b) {
        if (abs(inner_product(cbegin(b), cend(b), {1}, 0) == 
            abs(inner_product(cbegin(a), cend(a), {1}, 0))) {
            return distance(cbegin(nums), cbegin(nums)+find(cbegin(nums), cend(nums), a)) <
                distance(cbegin(nums), cbegin(nums)+find(cbegin(nums), cend(nums), b));
        } else {
            return abs(inner_product(cbegin(b), cend(b), {1}, 0) <
                abs(inner_product(cbegin(a), cend(a), {1}, 0));
        }
    });
    return nums;
}
// or
#include<numeric>
#include<algorithm>
#include<vector>
using namespace std;
vector<int> order_by_points(vector<int> nums){
    vector<pair<int, int>> v;
    for (int i : nums) {
        v.push_back({accumulate(cbegin(to_string(i)), cend(to_string(i)), 0), i});
    }
    sort(v.begin(), v.end());
    vector<int> res;
    for (int i : v) {
        res.push_back(i.second);
    }
    return res;
} 
// or
#include<numeric>
#include<algorithm>
#include<vector>
using namespace std;
vector<int> order_by_points(vector<int> nums){
    vector<pair<int, pair<int, int>>> v;
    for (int i : nums) {
        v.push_back({abs