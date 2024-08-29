/*
Write a function which sorts the given vector of integers
in ascending order according to the sum of their digits.
Note: if there are several items with similar sum of their digits,
order them based on their index in original vector.

For example:
>>> order_by_points({1, 11, -1, -11, -12}) == {-1, -11, 1, -12, 11}
>>> order_by_points({}) == {}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;
vector<int> order_by_points(vector<int> nums){
    vector<int> result;
    if(nums.empty()) return result;
    vector<int> v;
    for(int i=0; i<nums.size(); i++){
        int sum=0;
        int n=abs(nums[i]);
        while(n>0){
            sum+=n%10;
            n/=10;
        }
        v.push_back(sum);
    }
    for(int i=0; i<nums.size(); i++){
        int min_index=i;
        for(int j=i+1; j<nums.size(); j++){
            if(v[j]<v[min_index]) min_index=j;
        }
        int temp=nums[i];
        nums[i]=nums[min_index];
        nums[min_index]=temp;
        temp=v[i];
        v[i]=v[min_index];
        v[min_index]=temp;
    }
    for(int i=0; i<nums.size(); i++){
        result.push_back(nums[i]);
    }
    return result;
}

B:
/*
Write a function which sorts the given vector of integers
in ascending order according to the sum of their digits.
Note: if there are several items with similar sum of their digits,
order them based on their index in original vector.

For example:
>>> order_by_points({1, 11, -1, -11, -12}) == {-1, -11, 1, -12, 11}
>>> order_by_points({}) == {}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;
vector<int> order_by_points(vector<int> nums){
    vector<int> result;
    if(nums.empty()) return result;
    vector<int> v;
    for(int i=0; i<nums.size(); i++){
        int sum=0;
        int n=abs(nums[i]);
        while(n>0){
            sum+=n%10;
            n/=