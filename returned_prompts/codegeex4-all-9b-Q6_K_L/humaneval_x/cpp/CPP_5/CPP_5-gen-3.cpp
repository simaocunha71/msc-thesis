```cpp
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> intersperse(vector<int> numbers, int delimeter){ 
    vector<int> out;
    for (int i = 0; i < numbers.size(); i++) {
        out.push_back(numbers[i]);
        if (i != numbers.size() - 1) {
            out.push_back(delimeter);
        }
    }
    return out;
}
```