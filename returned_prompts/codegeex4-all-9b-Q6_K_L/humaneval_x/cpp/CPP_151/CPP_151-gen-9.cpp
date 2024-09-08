#include <vector>
#include <iostream>
using namespace std;

long long double_the_difference(const vector<int>& nums) {
    long long sum = 0;
    for (int num : nums) {
        if (num > 0 && num % 2 != 0) {
            sum += num * num;
        }
    }
    return sum;
}

