/*
Given vector of numbers (of at least two elements), apply a linear transform to that vector,
such that the smallest number will become 0 and the largest will become 1
>>> rescale_to_unit({1.0, 2.0, 3.0, 4.0, 5.0})
{0.0, 0.25, 0.5, 0.75, 1.0}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> rescale_to_unit(vector<float> numbers){ 
	int len = numbers.size();
	if (len < 2) 
	{
		return(numbers);
	}
	if (numbers[0] > numbers[1]){
		swap(numbers[0], numbers[1]);
	}
	float sum = numbers[0];
	for (int i = 1; i < len; i++) {
		sum += numbers[i];
	}
	float ratio = sqrt((pow(numbers[0],2) + pow(numbers[1] , 2)) / sum);
	if ((numbers[0] - numbers[1]) < 0)
	{
		return(numbers);
	}
	for (int i = 0; i < len; i++) {
		numbers[i] *= ratio;
	}
}
//Driver Code
int main(){
    vector<float> v1 = {3.7,4.2,6.5};
   // rescale_to_unit(v1); 
   cout<<rescale_to_unit(v1)<<endl;

	return (0);
}