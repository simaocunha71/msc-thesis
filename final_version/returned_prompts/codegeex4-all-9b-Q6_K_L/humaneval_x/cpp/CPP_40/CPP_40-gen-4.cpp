#include <iostream>
#include <vector>
using namespace std;

bool triples_sum_to_zero(vector<int> nums) {
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            for (int k = j + 1; k < nums.size(); k++) {
                if (nums[i] + nums[j] + nums[k] == 0) {
                    return true;
                }
            }
        }
    }
    return false;
}

int main() {
    vector<int> nums = {1, 2, 3, 7};
    bool result = triples_sum_to_zero(nums);
    cout << (result ? "true" : "false") << endl;
    return 0;
}

