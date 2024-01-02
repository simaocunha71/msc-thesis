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
	int n = xs.size();
	if (n == 1)return xs[0];
	vector<float> dx(n-1,0);
	for(int i=0;i<n-1;i++){
		dx[i] = 2 * pow(xs[i+1],2); // dx/dx
	}
	return (1/2) * (n*(pow(xs[0],3)+pow(dx,n)) - n*pow(xs[0],n-1));
	// (x^n)/(n!);
}
