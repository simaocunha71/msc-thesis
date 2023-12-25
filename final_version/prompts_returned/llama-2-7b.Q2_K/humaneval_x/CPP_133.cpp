/*
You are given a vector of numbers.
You need to return the sum of squared numbers in the given vector,
round each element in the vector to the upper int(Ceiling) first.
Examples:
For lst = {1,2,3} the output should be 14
For lst = {1,4,9} the output should be 98
For lst = {1,3,5,7} the output should be 84
For lst = {1.4,4.2,0} the output should be 29
For lst = {-2.4,1,1} the output should be 6


*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
int sum_squares(vector<float> lst){
	int res=0;
	for (auto i:lst) if(i>=0)res+=round(powf(lst[i],2));
	return res;
}
int main(){
	vector<float> v={1,3,5,7};
	int res=sum_squares(v);
	printf("%d\n",res);
	return 0;
}