/*
Given a vector of numbers, return the sum of squares of the numbers
in the vector that are odd. Ignore numbers that are negative or not integers.

double_the_difference({1, 3, 2, 0}) == 1 + 9 + 0 + 0 = 10
double_the_difference({-1, -2, 0}) == 0
double_the_difference({9, -2}) == 81
double_the_difference({0}) == 0  

If the input vector is empty, return 0.
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
long long double_the_difference(vector<float> lst){
	if(lst.size()==0)return 0;
    float* temp = new float[lst.size()];
    //copy the input vector values to temporary vector
    for(int i=0;i<lst.size();i++)temp[i]=(float)lst[i];
    
    //calculate and return sum of squares in a new vector
	for(int i=0;i<lst.size();i++){
		if((int)temp[i]%2==1){
        float x = powf(temp[i], 2);
			temp[i]=x;}
	}
    delete[] temp;
    
    return lst.back();
}
