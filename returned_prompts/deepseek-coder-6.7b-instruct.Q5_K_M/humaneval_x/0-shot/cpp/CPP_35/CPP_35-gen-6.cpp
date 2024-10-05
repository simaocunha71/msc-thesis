The problem is that the function max_element is not returning the maximum element in the given array. It returns the first element of the array. Also, the function main doesn't return the correct value.

Here is the correct code:

```cpp
#include<iostream>
#include<vector>
using namespace std;

float max_element(vector<float> l){
    float max=l[0];
    for(int i=0;i<l.size();i++){
        if(max<l[i]){
            max=l[i];
        }
    }
    return max;
}

int main(){
    vector<float> l;
    l.push_back(1);
    l.push_back(2);
    l.push_back(3);
    cout<< max_element(l) << endl;
    vector<float> m;
    m.push_back(5);
    m.push_back(3);
    m.push_back(-5);
    m.push_back(2);
    m.push_back(-3);
    m.push_back(3);
    m.push_