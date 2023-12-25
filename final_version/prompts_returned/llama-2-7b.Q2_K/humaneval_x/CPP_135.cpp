/*
Create a function which returns the largest index of an element which
is not greater than or equal to the element immediately preceding it. If
no such element exists then return -1. The given vector will not contain
duplicate values.

Examples:
can_arrange({1,2,4,3,5}) = 3
can_arrange({1,2,3}) = -1
*/
#include<stdio.h>
#include<vector>
using namespace std;
int can_arrange(vector<int> arr){
	if(arr[0]==-1) return -1;
	if(arr[0]>=arr[1])
	{
	  for (unsigned int i = 2; i < arr.size(); ++i) {
            if (arr[i+1] >= arr[i]) return -1;
        }
    } else {return 0;}
}
int main(){
	vector<int> vec;
	vec.push_back(-1);
	vec.push_back(5);
	vec.push_back(3);
	cout<<"can_arrange({1,2,4,3,5}) = ";
	printf("%d\n", can_arrange(vec));
	return 0;
}