    int i,j;
    
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;
}

This code works fine. But you can make it more efficient by checking the remaining elements in the loop. Because if the first element is not close to any other, then there is no need to check the second element, third element and so on. Here is the modified code.
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i=0;i<numbers.size()-1;i++){
        for (int j=i+1;j<numbers.size();j++){
            if (