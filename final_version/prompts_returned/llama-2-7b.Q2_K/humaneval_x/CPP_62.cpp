/*
xs represent coefficients of a polynomial.
xs{0} + xs{1} * x + xs{2} * x^2 + ....
 Return derivative of this polynomial in the same form.
>>> derivative({3, 1, 2, 4, 5})
{1, 4, 12, 20}
>>> derivative({1, 2, 3})
{2, 6}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> derivative(vector<float> xs){
	int n=xs.size();
	float dp=0., sumdp=0.;
	float x, p[MAXN+1];
	if (n==0) return vector<float>();
	for (int i=0;i<n-1;++i){
		x=xs.at(i);
		p[i]=1.;
	}
	if (n>2){
		sumdp+= pow(xp, n) * p[n-1];
		for (int j=0;j<n-1;++j){
			x=xs.at(j);
			p[j]=1.;
		}
		for (int i=0;i<n-2;++i) {
			p[i]+=pow(xp, n-1-i)*sumdp/pow(xp, n);
		}
	}else{
		p[0]=1.;
	}
	return vector<float>(p+1); // vector of pointers, each is a float
}