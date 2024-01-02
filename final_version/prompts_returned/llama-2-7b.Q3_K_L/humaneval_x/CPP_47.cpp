/*
Return median of elements in the vector l.
>>> median({3, 1, 2, 4, 5})
3
>>> median({-10, 4, 6, 1000, 10, 20})
15.0
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){
	if(l.size()%2==0) {
	  float *x=new float[l.size()];
    	for (int i=0;i<l.size();i++) x[i]=l[i];
      median(x);
      delete [] x;
    }
	float median =*std::min_element(l.begin(),l.end());
	return median;
}
