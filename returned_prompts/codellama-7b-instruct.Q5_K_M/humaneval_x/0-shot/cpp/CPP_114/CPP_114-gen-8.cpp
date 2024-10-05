#include <vector>
#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> nums;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        nums.push_back(num);
    }

    int start = 0, end = 0;
    int min_sum = nums[0];
    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = i; j < n; j++) {
            sum += nums[j];
            if (sum < min_sum) {
                min_sum = sum;
                start = i;
                end = j;
            }
        }
    }

    cout << min_sum << endl;
    return 0;
}

