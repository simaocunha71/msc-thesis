/*
Write a function called "filter_array" which takes an array of integers and a number
as input, and returns a new array made up of only those numbers which are divisible 
by the number.
Examples:
filter_array([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
filter_array([1, 2, 3, 4, 5, 6], 3) == [3]
filter_array([1, 2, 3, 4, 5, 6], 7) == []
*/
#include <iostream>
#include <vector>
using namespace std;

vector<int> filter_array(vector<int> arr, int divisor) {
    vector<int> result;
    for (auto i : arr) {
        if (i % divisor == 0) {
            result.push_back(i);
        }
    }
    return result;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5, 6};
    vector<int> result = filter_array(arr, 2);
    for (auto i : result) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}

