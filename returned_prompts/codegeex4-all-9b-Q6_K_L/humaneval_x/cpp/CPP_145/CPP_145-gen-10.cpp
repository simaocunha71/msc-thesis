#include <bits/stdc++.h>
#include <iostream>
using namespace std;

vector<int> order_by_points(vector<int> nums) {
    vector<pair<int, int>> temp;
    for (int i = 0; i < nums.size(); i++) {
        temp.push_back(make_pair(nums[i], i));
    }
    sort(temp.begin(), temp.end(), [](pair<int, int> a, pair<int, int> b) {
        int sumA = 0, sumB = 0;
        for (int digit : to_string(a.first)) {
            sumA += digit - '0';
        }
        for (int digit : to_string(b.first)) {
            sumB += digit - '0';
        }
        if (sumA == sumB) {
            return a.second < b.second;
        }
        return sumA < sumB;
    });
    vector<int> result;
    for (auto &p : temp) {
        result.push_back(p.first);
    }
    return result;
}
int main() {
    vector<int> nums = {1, 11, -1, -11, -12};
    vector<int> sorted_nums = order_by_points(nums);
    for (int num : sorted_nums) {
        cout << num << " ";
    }
    return 0;
}
B:
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

vector<int> order_by_points(vector<int> nums) {
    vector<pair<int, int>> temp;
    for (int i = 0; i < nums.size(); i++) {
        temp.push_back(make_pair(nums[i], i));
    }
    sort(temp.begin(), temp.end(), [](pair<int, int> a, pair<int, int> b) {
        int sumA = 0, sumB = 0;
        for (int digit : to_string(a.first)) {
            sumA += digit - '0';
        }
        for (int digit : to_string(b.first)) {
            sumB += digit - '0';
        }
        if (sumA == sumB) {
            return a.second < b.second;
        }
        return sumA < sumB;
    });
    vector<int> result;
    for (auto &p : temp) {
        result.push_back(p.first);
    }
    return result;
}
int main() {
    vector<int> nums = {1, 11, -1, -11, -12};
    vector<int