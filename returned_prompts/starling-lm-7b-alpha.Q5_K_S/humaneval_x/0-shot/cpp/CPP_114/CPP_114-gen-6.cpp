    long long ret = LONG_MAX;
    long long sum = 0;
    for(int i = 0; i < nums.size(); ++i){
        sum += nums[i];
        if(sum < ret) ret = sum;
        if(sum < 0) sum = 0;
    }
    return ret;
}

int main(void){
    vector<long long> nums = {2, 3, 4, 1, 2, 4};
    printf("%lld\n", minSubArraySum(nums));
    return 0;
}







*/
#include <iostream>
using namespace std;

int main() {
	int n;
	cin>>n;
	int a[n];
	for(int i=0;i<n;i++)
		cin>>a[i];
	int mn=INT_MAX;
	for(int i=0;i<n;i++)
	{
		int sum=0;
		for(int j=i;j<n;j++)
		{
			sum+=a[j];
			mn=min(mn,sum);
		}
	}
	cout<<mn<<endl;
	return 0;
}


























```