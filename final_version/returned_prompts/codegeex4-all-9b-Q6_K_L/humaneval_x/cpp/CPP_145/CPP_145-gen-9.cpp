#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
vector<int> order_by_points(vector<int> nums){
    vector<pair<int, int>> sums;
    for (int i = 0; i < nums.size(); i++) {
        int sum = 0;
        int num = abs(nums[i]);
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        sums.push_back(make_pair(sum, i));
    }
    sort(sums.begin(), sums.end());
    vector<int> result;
    for (int i = 0; i < sums.size(); i++) {
        result.push_back(nums[sums[i].second]);
    }
    return result;
}
int main(){
    vector<int> nums = {-1, -11, 1, -12, 11};
    vector<int> sorted_nums = order_by_points(nums);
    for (int i = 0; i < sorted_nums.size(); i++) {
        cout << sorted_nums[i] << " ";
    }
    cout << endl;
    return 0;
}

C:
#include<iostream>
#include<vector>
using namespace std;
int sum_of_digits(int num){
    int sum = 0;
    while(num > 0){
        sum += num % 10;
        num /= 10;
    }
    return sum;
}
vector<int> order_by_points(vector<int> nums){
    vector<pair<int, int>> sums;
    for(int i = 0; i < nums.size(); i++){
        sums.push_back(make_pair(sum_of_digits(nums[i]), i));
    }
    sort(sums.begin(), sums.end());
    vector<int> result;
    for(int i = 0; i < sums.size(); i++){
        result.push_back(nums[sums[i].second]);
    }
    return result;
}
int main(){
    vector<int> nums = {1, 11, -1, -11, -12};
    vector<int> sorted_nums = order_by_points(nums);
    for(int i = 0; i < sorted_nums.size(); i++){
        cout<<sorted_nums[i]<<" ";
    }
    return 0;
}

D:
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> order_by_points(vector<int> nums){
    vector<pair<int,int>> sums;
    for(int i=0;i<nums.size();i++){
        int sum