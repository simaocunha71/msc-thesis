/*
Return true is vector elements are monotonically increasing or decreasing.
>>> monotonic({1, 2, 4, 20})
true
>>> monotonic({1, 20, 4, 10})
false
>>> monotonic({4, 1, 0, -10})
true
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool monotonic(vector<float> l){
	if(l.size()==0) return true;
	int flag=2;
	for(int i=1;i<l.size();i++)
	{
		if(l[i]>=l[i-1])
			flag=flag%2+1;
		else 
			flag=2;
	}
	return flag==0;
}
int main(){
	float t,m=-5.0,b=-3.0;
	vector<float> v={t,m,-3.0};
	printf("The vector %f is monotonically increasing\n",v[1]);
	if(monotonic(v)) printf("The vector %f is monotonically decreasing\n",v[1]);
}
