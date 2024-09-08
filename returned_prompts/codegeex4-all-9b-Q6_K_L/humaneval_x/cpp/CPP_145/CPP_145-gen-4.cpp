#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<int> order_by_points(vector<int> nums){
    vector<pair<int,int>> arr;
    for(int i=0;i<nums.size();i++){
        int sum=0;
        int num=nums[i];
        while(num!=0){
            sum+=num%10;
            num/=10;
        }
        arr.push_back({sum,i});
    }
    sort(arr.begin(),arr.end());
    vector<int> ans;
    for(int i=0;i<arr.size();i++){
        ans.push_back(nums[arr[i].second]);
    }
    return ans;
}