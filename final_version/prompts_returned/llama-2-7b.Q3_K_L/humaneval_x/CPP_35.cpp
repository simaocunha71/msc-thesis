/*
Return maximum element in the vector.
>>> max_element({1, 2, 3})
3
>>> max_element({5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})
123
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
float max_element(vector<float> l){
	if(l.size()==0) return -999.f, -999.f;
	//find the largest element among the first k elements of an array
	int i=1,j=0,k=1;
	while (i<l.size())
	{
		float a = l[i];
		if(a>max_element(l))
		{
			j++;
		}
		i+=j;
		if(k>j)
		{
			k=j;
		}
	}
	float ans = l[1];
	return max_element(l),ans;
}
int main(){
	vector<float> v(1);
	v.push_back(-999.f);
	v[0]=-999.f;
	v.push_back(-999.f);
	printf("%f\n",max_element(*v));//it will always return -999 because max element in this case is 0
	for(int i=1;i<7;i++)
	{
		float a = (double)rand();
		v.push_back((a/a+1)*-1*1000+1);//put random numbers between -1 and 1 and add 1 to it
	}
	printf("%f\n",max_element(*v));
	return 0;
}