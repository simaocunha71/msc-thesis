```cpp
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
#include<algorithm>
#include<stdlib.h>
vector<int> intersperse(vector<int> numbers, int delimeter){ 
    if (numbers.size()==0) return numbers;
    vector<int> out={numbers[0],delimeter};
    for (int i=1;i<numbers.size();i++) {
        out.push_back(numbers[i]);
        out.push_back(delimeter);
    }
    return out;
}
```