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
    float acc=0,sum=0;//acc is the sum and sum will be the sum of squared odd numbers
    for(int i=0;i<lst.size();i++){
        if (fabs(lst[i]) < EPSILON)continue;   //ignore 0s and negatives
	float diff= lst[i]%2 -1 ;//we will only consider the odd no of type
	if(!isnan(diff)){sum+=diff*diff;}
        else sum +=fabs(lst[i]);
    }
    return sum;
}
int main(){
	vector<float> v{1, 3, 2, -0};
	int i,j=0;//we will consider only the odd no from now as the j value is the index of the vector which stores the odds
	double_the_difference(v);
}
