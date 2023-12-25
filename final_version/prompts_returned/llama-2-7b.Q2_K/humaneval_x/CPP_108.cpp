/*
Write a function count_nums which takes a vector of integers and returns
the number of elements which has a sum of digits > 0.
If a number is negative, then its first signed digit will be negative:
e.g. -123 has signed digits -1, 2, and 3.
>>> count_nums({}) == 0
>>> count_nums({-1, 11, -11}) == 1
>>> count_nums({1, 1, 2}) == 3
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
int count_nums(vector<int> n){
	int ans = 0;
	for(int i=n.begin();i!=n.end();++i)
        if(*i != (int)(floor((*i-1)*10))){
            ans++;
        }
    return ans;
}
int main(){
     vector<int> n = {4,-1,9,-2};
	 printf("%d\n",count_nums(n));
}