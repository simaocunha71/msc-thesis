/*
In this Kata, you have to sort a vector of non-negative integers according to
number of ones in their binary representation in ascending order.
For similar number of ones, sort based on decimal value.

It must be implemented like this:
>>> sort_vector({1, 5, 2, 3, 4}) == {1, 2, 3, 4, 5}
>>> sort_vector({-2, -3, -4, -5, -6}) == {-6, -5, -4, -3, -2}
>>> sort_vector({1, 0, 2, 3, 4}) == {0, 1, 2, 3, 4}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> sort_array(vector<int> arr){
    vector<int> result;
    for (int i = 0; i < arr.size(); i++) {
        result.push_back(arr[i]);
    }
    for (int i = 0; i < result.size(); i++) {
        for (int j = 0; j < result.size() - 1; j++) {
            if (result[j] == result[j + 1]) {
                continue;
            }
            if (count_ones(result[j]) == count_ones(result[j + 1]) && result[j] > result[j + 1]) {
                int temp = result[j];
                result[j] = result[j + 1];
                result[j + 1] = temp;
            }
            if (count_ones(result[j]) < count_ones(result[j + 1])) {
                int temp = result[j];
                result[j] = result[j + 1];
                result[j + 1] = temp;
            }
        }
    }
    return result;
}
int count_ones(int n) {
    int count = 0;
    while (n > 0) {
        n &= (n -