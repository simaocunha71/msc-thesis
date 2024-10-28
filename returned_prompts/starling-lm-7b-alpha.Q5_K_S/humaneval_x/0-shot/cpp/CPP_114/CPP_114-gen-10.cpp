    long long mins=nums[0];
    long long minl=nums[0];
    long long sum=nums[0];
    for(int i=1;i<nums.size();i++){
        sum+=nums[i];
        if(sum<mins){
            mins=sum;
            minl=i;
        }
        if(sum>mins)
            sum-=nums[minl];
    }
    return mins;
}
int main(){
    vector<long long> nums={2, 3, 4, 1, 2, 4};
    printf("%d\n",minSubArraySum(nums));
    return 0;
}

*/

#include <iostream>
#include <vector>
using namespace std;

long long minSubArraySum(vector<long long>& nums) {
    long long mins = nums[0];
    long long minl = nums[0];
    long long sum = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        sum += nums[i];
        if (sum < mins) {
            mins = sum;
            minl = i;
        }
        if (sum > mins)
            sum -= nums[minl];
    }
    return mins;
}

int main() {
    vector<long long> nums = {2, 3, 4, 1, 2, 4};
    cout << minSubArraySum(nums) << endl;
    return 0;
}
























































































































