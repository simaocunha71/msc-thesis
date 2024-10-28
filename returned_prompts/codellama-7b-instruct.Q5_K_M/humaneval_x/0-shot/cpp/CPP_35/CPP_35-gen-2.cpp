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
	float a=l[0];
	for(int i=0;i<l.size();i++)
		if(l[i]>a)
			a=l[i];
	return a;
}
int main(){
	vector<float> l;
	for(int i=0;i<10;i++)
		l.push_back(rand()%10);
	printf("%f",max_element(l));
	return 0;
}

