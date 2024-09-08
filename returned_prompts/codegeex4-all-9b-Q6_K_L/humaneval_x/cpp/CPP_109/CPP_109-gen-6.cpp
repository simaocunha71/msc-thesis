
Here is a solution in C++ that works by comparing the first element of the array with the first element of the sorted array:

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

bool move_one_ball(vector<int> arr) {
    vector<int> sorted_arr(arr.begin(), arr.end());
    sort(sorted_arr.begin(), sorted_arr.end());

    for(int i = 0; i < arr.size(); i++) {
        if(arr[i] != sorted_arr[i % sorted_arr.size()]) {
            return false;
        }
    }

    return true;
}

int main() {
    vector<int> arr = {3, 4, 5, 1, 2};
    cout << move_one_ball(arr) << endl;
    return 0;
}

This solution sorts the array and then checks if the sorted array can be achieved by shifting the original array. If every element in the original array matches the corresponding element in the sorted array when shifted appropriately, the function returns true. Otherwise, it returns false.