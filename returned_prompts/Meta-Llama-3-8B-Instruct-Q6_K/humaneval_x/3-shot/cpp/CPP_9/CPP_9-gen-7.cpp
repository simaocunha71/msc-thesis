    vector<int> max_rolling;
    int max_value=INT_MIN;
    for (int i=0;i<numbers.size();i++)
    {
        max_value=max(max_value, numbers[i]);
        max_rolling.push_back(max_value);
    }
    return max_rolling;
}
// alternative
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> rolling_max(vector<int> numbers){
    vector<int> max_rolling;
    int max_value=INT_MIN;
    for (int i=0;i<numbers.size();i++)
    {
        max_value=max(max_value, numbers[i]);
        max_rolling.push_back(max_value);
    }
    return max_rolling;
}
