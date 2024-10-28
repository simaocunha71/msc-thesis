/*
In this Kata, you have to sort a vector of non-negative integers according to
number of ones in their binary representation in ascending order.
For similar number of ones, sort based on decimal value.

It must be implemented like this:
>>> sort_vector({1, 5, 2, 3, 4}) == {1, 2, 3, 4, 5}
>>> sort_vector({-2, -3, -4, -5, -6}) == {-6, -5, -4, -3, -2}
>>> sort_vector({1, 0, 2, 3, 4}) == {0, 1, 2, 3, 4}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> sort_array(vector<int> arr){
vector<int> v;
for(int i=0;i<arr.size();i++)
{
v.push_back(arr[i]);
}
sort(v.begin(),v.end(),[](int a,int b){
int a1=0,b1=0;
while(a)
{
a1++;
a=a&(a-1);
}
while(b)
{
b1++;
b=b&(b-1);
}
return a1==b1?a<b:a1<b1;
});
return v;
}







