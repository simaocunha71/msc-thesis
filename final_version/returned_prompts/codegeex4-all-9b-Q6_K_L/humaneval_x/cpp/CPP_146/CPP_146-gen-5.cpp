#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;
int specialFilter(vector<int> nums){
    int count = 0;
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] > 10 && abs(nums[i]) % 10 % 2 == 1 && abs(nums[i]) / pow(10, floor(log10(abs(nums[i])))) % 2 == 1){
            count++;
        }
    }
    return count;
}
