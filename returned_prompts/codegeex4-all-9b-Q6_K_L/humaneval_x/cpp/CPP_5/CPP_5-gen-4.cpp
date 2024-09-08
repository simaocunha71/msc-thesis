```cpp
#include<vector>
#include<iostream>
using namespace std;
vector<int> intersperse(vector<int> numbers, int delimeter){ 
    vector<int> out;
    for (int i = 0; i < numbers.size(); i++){
        out.push_back(numbers[i]);
        if (i != numbers.size()-1)
            out.push_back(delimeter);
    }
    return out;
}
int main() {
    vector<int> test = intersperse({1, 2, 3}, 4);
    for (int i = 0; i < test.size(); i++)
        cout << test[i] << " ";
    return 0;
}
```

这是C++的解决方案。