
}
*/

//Solution:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;

bool compare(pair<int, int> p1, pair<int, int> p2){
    if(p1.second < p2.second)
        return true;
    if(p2.second < p1.second)
        return false;
    return p1.first < p2.first;
}

vector<int> order_by_points(vector<int> nums){
    vector<pair<int, int>> nums_with_points;
    for(int i = 0; i < nums.size(); i++){
        int sum = 0;
        int num = abs(nums[i]);
        while(num){
            sum += num % 10;
            num /= 10;
        }
        nums_with_points.push_back(make_pair(nums[i], sum));
    }
    sort(nums_with_points.begin(), nums_with_points.end(), compare);
    vector<int> sorted_nums;
    for(int i = 0; i < nums_with_points.size(); i++){
        sorted_nums.push_back(nums_with_points[i].first);
    }
    return sorted_nums;
}

int main(){
    vector<int> nums = {1, 11, -1, -11, -12};
    vector<int> sorted_nums = order_by_points(nums);
    for(int i = 0; i < sorted_nums.size(); i++){
        printf("%d ", sorted_nums[i]);
    }
    return 0;
}

In the above solution, we first calculate the sum of digits for each number in the input vector and then we store the number and its sum in a pair. After that we sort the pairs based on the sum of digits. If two pairs have the same sum of digits, we compare their indices in the original vector. Finally, we return the