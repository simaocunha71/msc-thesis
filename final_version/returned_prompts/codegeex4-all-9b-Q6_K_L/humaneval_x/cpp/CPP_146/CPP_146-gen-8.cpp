#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
int specialFilter(vector<int> nums){
    int count=0;
    for(int i=0;i<nums.size();i++){
        if(nums[i]>10){
            string str = to_string(nums[i]);
            if(str[0] % 2 != 0 && str[str.length()-1] % 2 != 0){
                count++;
            }
        }
    }
    return count;
}