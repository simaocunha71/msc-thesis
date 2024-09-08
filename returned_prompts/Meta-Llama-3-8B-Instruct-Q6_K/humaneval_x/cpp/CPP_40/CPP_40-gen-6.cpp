    vector<int>::iterator it = l.begin();
    for (; it != l.end(); ++it) {
        vector<int>::iterator it2 = it + 1;
        for (; it2 != l.end(); ++it2) {
            vector<int>::iterator it3 = it2 + 1;
            for (; it3 != l.end(); ++it3) {
                if (*it + *it2 + *it3 == 0) {
                    return true;
                }
            }
        }
    }
    return false;
}

int main() {
    vector<int> l1 = {1, 3, 5, 0};
    printf("%d\n", triples_sum_to_zero(l1));
    vector<int> l2 = {1, 3, -2, 1};
    printf("%d\n", triples_sum_to_zero(l2));
    vector<int> l3 = {1, 2, 3, 7};
    printf("%d\n", triples_sum_to_zero(l3));
    vector<int> l4 = {2, 4, -5, 3, 9, 7};
    printf("%d\n", triples_sum_to_zero(l4));
    vector<int> l5 = {1};
    printf("%d\n", triples_sum_to_zero(l5));
    return 0;
}
B:
    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;

    bool triples_sum_to_zero(const vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (size_t i = 0; i < nums.size() - 2; ++i) {
            size_t left = i + 1;
            size_t right = nums.size() - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    return true;
                } else if (sum < 0) {
                    ++left;
                } else {
                    --right;
                }
            }
        }
        return false;
    }

    int main() {
        vector<int> l1 = {1, 3, 5, 0};
        cout << (triples_sum_to_zero(l1) ? "true" : "false") << endl;
        vector<int> l2 = {1, 3, -2, 1};
        cout << (triples