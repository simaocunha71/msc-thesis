    vector<float> positive_nums;
    for(int i=0; i<l.size(); i++)
        if(l[i] > 0)
            positive_nums.push_back(l[i]);
    return positive_nums;
}

int main(){
    vector<float> l = {5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10};
    vector<float> positive_nums = get_positive(l);
    for(int i=0; i<positive_nums.size(); i++)
        printf("%f ", positive_nums[i]);
    return 0;
}


A: The original Python code uses sets, which are unordered collections of unique elements. In C++, we use vectors which are ordered collections of elements. Therefore, you cannot use the same code as is. Instead, I will provide the C++ code that gets only the positive numbers from a vector.

C++ Code:

```cpp
#include<iostream>
#include<vector>
using namespace std;

vector<int> get_positive(vector<int> l){
    vector<int> positive_nums;
    for(int i=0; i<l.size(); i++)
        if(l[i] > 0)
            positive_nums.push_back(l[i]);
    return positive_nums;
}

int main(){
    vector<int> l = {-1, 2, -4, 5, 6};
    vector<int> positive_nums = get_positive(l);
    for(int i=0; i<positive_nums.size(); i++)
        cout << positive_nums[i] << " ";
    return 0;
}
```

This will output: 2 5 6

In this C++ code, we have a function get_positive() that takes in a vector of integers as a parameter. It then iterates over each element in the vector, checking if it is positive. If it is, it is added to a new vector named positive_nums. This