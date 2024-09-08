#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> rescale_to_unit(vector<float> numbers){ 
    vector<float> rescaled;
    float min = numbers[0];
    float max = numbers[0];
    for(int i = 0; i < numbers.size(); i++){
        if(numbers[i] < min){
            min = numbers[i];
        }
        if(numbers[i] > max){
            max = numbers[i];
        }
    }
    for(int i = 0; i < numbers.size(); i++){
        rescaled.push_back((numbers[i]-min)/(max-min));
    }
    return rescaled;
}
int main(){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};
    vector<float> rescaled = rescale_to_unit(numbers);
    for(int i = 0; i < rescaled.size(); i++){
        printf("%.2f ", rescaled[i]);
    }
    return 0;
}

