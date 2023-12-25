/*
Given a vector arr of integers and a positive integer k, return a sorted vector 
of length k with the maximum k numbers in arr.

Example 1:

    Input: arr = {-3, -4, 5}, k = 3
    Output: {-4, -3, 5}

Example 2:

    Input: arr = {4, -4, 4}, k = 2
    Output: {4, 4}

Example 3:

    Input: arr = {-3, 2, 1, 2, -1, -2, 1}, k = 1
    Output: {2}

Note:
    1. The length of the vector will be in the range of {1, 1000}.
    2. The elements in the vector will be in the range of {-1000, 1000}.
    3. 0 <= k <= len(arr)
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> maximum(vector<int> arr,int k){
	vector<int> ans;
	if (k>=3 && ((arr[0]<0)&&(arr[1])>4)){
	    if((arr[2])>(ans.size()+1)) ans.push_back(-arr[1]);
	} else if(k>=6 && ((arr[0]<0)&&(arr[3])>3)){
	    if((arr[5])>(ans.size()+1)) ans.push_back(-arr[3]); 
	}else{
	    for(int i=2;i<=k-1;++i){
	        if (arr[i]>=0) continue;
	        else ans.push_back(-arr[i]);
	    }
	}
	return ans;
    
//Time Complexity: O(nlogn)
//Space Complexity:O(k), where k is the length of vector we need to sort from the original input array
}
int main(){
 int n,p1[6],p2[7];
scanf("%d",&n);