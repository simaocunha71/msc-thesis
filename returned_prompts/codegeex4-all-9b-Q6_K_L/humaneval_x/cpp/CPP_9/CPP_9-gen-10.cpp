#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<int> rolling_max(vector<int> numbers){
    vector<int> res;
    int max=numbers[0];
    res.push_back(max);
    for(int i=1;i<numbers.size();i++){
        if(numbers[i]>max){
            max=numbers[i];
            res.push_back(max);
        }else{
            res.push_back(max);
        }
    }
    return res;
}
这段代码有问题，应该返回res，而返回的是max
