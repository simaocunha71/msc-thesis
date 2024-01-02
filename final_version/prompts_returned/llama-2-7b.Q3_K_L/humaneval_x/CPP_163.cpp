/*
Given two positive integers a and b, return the even digits between a
and b, in ascending order.

For example:
generate_integers(2, 8) => {2, 4, 6, 8}
generate_integers(8, 2) => {2, 4, 6, 8}
generate_integers(10, 14) => {}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> generate_integers(int a,int b){
	vector<int> ans;
	for (int i = a ; i < b ; ++i) {
	  if (i %2 ==0 ){
		ans.push_back(i);
	  }
	}
	return ans;
}
int main(){
	int t,n,a[10],b[10];
	scanf("%d",&t);
	while (t--){
		scanf("%d %d",&n,&a[1]);
		if(n==0) break;
		b[1]=a[1]+1;
		int sum=0;
		for (int i = 2 ; i < n+1 ; ++i){
		  if((a[sum]%2 == 0) &&(b[sum]%2 == 0)){
		  	printf(" %d\n",a[sum]);
		    sum++;
		  }
		}
	}
return 0;
}
