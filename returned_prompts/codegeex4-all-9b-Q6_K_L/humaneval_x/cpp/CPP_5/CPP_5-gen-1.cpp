#include<stdio.h>
#include<vector>
using namespace std;
vector<int> intersperse(vector<int> numbers, int delimeter){ 
    vector<int> result;
    if(numbers.empty())
        return result;
    for(int i=0; i<numbers.size(); i++){
        result.push_back(numbers[i]);
        result.push_back(delimeter);
    }
    result.pop_back();
    return result;
}
