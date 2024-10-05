    vector<pair<int,int>> v;
    for(int i=0;i<nums.size();i++){
        int sum=0;
        int num=abs(nums[i]);
        while(num>0){
            sum+=num%10;
            num/=10;
        }
        v.push_back(make_pair(sum,nums[i]));
    }
    sort(v.begin(),v.end());
    vector<int> res;
    for(int i=0;i<v.size();i++){
        res.push_back(v[i].second);
    }
    return res;
}
*/

// CORRECT ANSWER

#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;

int sum_of_digits(int n){
    n = abs(n);
    int sum = 0;
    while(n > 0){
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

vector<int> order_by_points(vector<int> nums){
    sort(nums.begin(), nums.end(), [](int a, int b){
        int sum_a = sum_of_digits(a);
        int sum_b = sum_of_digits(b);
        if(sum_a == sum_b)
            return a < b;
        return sum_a < sum_b;
    });
    return nums;
}

int main(){
    vector<int> nums = {1, 11, -1, -11, -12};
    vector<int> res = order_by_points(nums);
    for(int num : res){
        printf("%d ", num);
    }
    return 0;
}

*/

// CORRECT ANSWER

#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std