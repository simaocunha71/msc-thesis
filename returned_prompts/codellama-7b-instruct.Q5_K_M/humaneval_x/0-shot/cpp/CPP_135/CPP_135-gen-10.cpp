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

int i;
int n = arr.size();
int max = -1;
int temp;
for(i=0;i<n-1;i++){
if(arr[i] < arr[i+1]){
temp = i;
if(max < temp){
max = temp;
}
}
}
if(max == -1)
return -1;
else
return max;
}

int main(){
int t;
scanf("%d",&t);
while(t--){
int n;
scanf("%d",&n);
vector<int> a(n);
for(int i=0;i<n;i++){
scanf("%d",&a[i]);
}
printf("%d\n",can_arrange(a));
}
return 0;
}
