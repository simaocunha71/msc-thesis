#include<stdio.h>
#include<vector>
#include<climits>
using namespace std;
vector<int> rolling_max(vector<int> numbers){
    vector<int> output;
    int max = INT_MIN;
    for(int i=0;i<numbers.size();i++){
        max = max>numbers[i]?max:numbers[i];
        output.push_back(max);
    }
    return output;
}