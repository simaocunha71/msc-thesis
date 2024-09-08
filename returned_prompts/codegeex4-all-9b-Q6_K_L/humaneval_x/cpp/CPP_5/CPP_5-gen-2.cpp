```cpp
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> intersperse(vector<int> numbers, int delimeter){ 
    vector<int> result;
    if(numbers.size() == 0) return result;
    for(int i = 0; i < numbers.size(); i++){
        result.push_back(numbers[i]);
        if(i != numbers.size() - 1) result.push_back(delimeter);
    }
    return result;
}
```