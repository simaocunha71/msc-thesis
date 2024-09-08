/*
Write a function which sorts the given vector of integers
in ascending order according to the sum of their digits.
Note: if there are several items with similar sum of their digits,
order them based on their index in original vector.

For example:
>>> order_by_points({1, 11, -1, -11, -12}) == {-1, -11, 1, -12, 11}
>>> order_by_points({}) == {}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;

// 1. sort by sum of digits
// 2. sort by index
// 3. sort by absolute value
// 4. sort by negative
// 5. sort by positive
// 6. sort by even
// 7. sort by odd

// 1. sort by sum of digits
vector<int> order_by_points(vector<int> nums){
    sort(nums.begin(), nums.end(), [](int a, int b){
        int sum_a = 0;
        int sum_b = 0;
        int abs_a = abs(a);
        int abs_b = abs(b);
        while(abs_a > 0){
            sum_a += abs_a % 10;
            abs_a = abs_a / 10;
        }
        while(abs_b > 0){
            sum_b += abs_b % 10;
            abs_b = abs_b / 10;
        }
        return sum_a < sum_b;
    });
    return nums;
}

vector<int> order_by_points(vector<int> nums){
    sort(nums.begin(), nums.end(), [](int a, int b){
        int sum_a = 0;
        int sum_b = 0;
        int abs_a = abs(a);
        int abs_b = abs(b);
        while(abs_a > 0){
            sum_a += abs_a % 10;
            abs_a = abs_a / 10;
        }
        while(abs_b > 0){
            sum_b += abs_b % 10;
            abs_b = abs_b / 10;
        }
        return sum_a < sum_b;
    });
    return nums;
}

vector<int> order_by_points(vector<int> nums){
    sort(nums.begin(), nums.end(), [](int a, int b){
        int sum_a = 0;
        int sum_b = 0;
        int abs_a = abs(a);
        int abs_b = abs(b);
        while(abs_a > 