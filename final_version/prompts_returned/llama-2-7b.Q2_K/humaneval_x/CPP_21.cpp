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
	if (len ==0)return vector<float>();
	float min;
	float max;  
    for (int i = 0; i < len -1; ++i) {
        if (numbers[i] < min || max < numbers[i])
            continue;
        if (max == 0 && min != 0 )min = 0 ; 
		max= max > numbers[i-1] ? max : numbers[i-1];
    }  
    float scale_factor =1/(max + min);
	vector<float> rescale(len -1 );
	for (int i = 0; i < len ; ++i) {
        if (numbers[i] == max || numbers[i] == 0.0f )continue;
        float x = scale_factor *numbers[i];     
	rescale[i-1] = x; 
    }    
    return rescale;
}
int main() {
     vector<float> vn (4);
     for (unsigned int i =0 ; i < vn.size(); i++)
        vn.at(i) = rand();  
	cout<<"before min max scale_factor is :"<<vn[2]<<""<<vn[1] << ""<<vn[4]<<endl;
    vector<float> rescaled =rescale_to_unit(vn);
	for (unsigned int i =0 ; i < vn.size(); i++)
        cout<<"after min