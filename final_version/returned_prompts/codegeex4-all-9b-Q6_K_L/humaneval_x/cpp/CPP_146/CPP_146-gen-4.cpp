#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
int specialFilter(vector<int> nums){
    int count = 0;
    for(int i=0; i<nums.size(); i++){
        if(nums[i]>10){
            int firstDigit = nums[i]/100;
            int lastDigit = nums[i]%10;
            if(firstDigit%2!=0 && lastDigit%2!=0){
                count++;
            }
        }
    }
    return count;
}

