    vector<int>ans(2);
    for(int i=1;i<=n;i++){
        string str=to_string(i);
        if(str==string(str.rbegin(),str.rend())){
            if(i%2==0)ans[0]++;
            else ans[1]++;
        }
    }
    return ans;
}

int main(){
    int n;
    scanf("%d",&n);
    vector<int>ans=even_odd_palindrome(n);
    printf("%d %d\n",ans[0],ans[1]);
    return 0;
}

*/


/*
Given an array of integers, find the max sum of a contiguous subarray within the array.

Example 1:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: The input array is [-2,1,-3,4,-1,2,1,-5,4]. The subarray [4,-1,2,1] has the largest sum = 6.

Note:

1. -10^5 <= number <= 10^5
2. The length of the array is at most 30.

*/

#include<vector>
#include<algorithm>
using namespace std;
int maxSubArray(vector<int>& nums) {
    int maxsum=nums[0];
    int sum=nums[0];
    for(int i=0;i<nums.size();i++){
        if(nums[i]<0){
            sum=0;
        }else{
            sum+=nums[i];
        }
        maxsum=max(sum,maxsum);
    }
    return maxsum;
}

int main(){
    vector<int>nums;
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        int temp;
        scanf("%d",&temp);
        nums.push_back(temp);
    }
    int ans=max