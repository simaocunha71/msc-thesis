In C++, you can use the `std::vector` class to store the numbers. The `std::abs` function can be used to compute the absolute difference between two numbers. In your case, you want to check if there are two numbers in the vector that have an absolute difference less than the given threshold. If such numbers exist, the function should return true; otherwise, it should return false.

Here's the corrected code:

```cpp
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold){
    for(int i=0;i<numbers.size()-1;i++){
        for(int j=i+1;j<numbers.size();j++){
            if(abs(numbers[i]-numbers[j])<threshold)
                return true;
        }
    }
    return false;
}

int main(){
    vector<float> numbers={1.0, 2.8, 3.0, 4.0, 5.0, 2.0};
    float threshold=0.3;
    if(has_close_elements(numbers, threshold))
        cout<<"True"<<endl;
    else
        cout<<"False"<<endl;
    return 0;
}
```

This code will output "True" if there are two numbers in the vector that are closer to each other than the given threshold, and "False" otherwise.
