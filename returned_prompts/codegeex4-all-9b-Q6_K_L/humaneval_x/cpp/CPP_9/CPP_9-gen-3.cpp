#include <vector>
#include <algorithm>
using namespace std;

vector<int> rolling_max(vector<int> numbers){
    vector<int> maxes;
    int max = INT_MIN;
    for(int i=0; i<numbers.size(); i++){
        if(numbers[i] > max){
            max = numbers[i];
            maxes.push_back(max);
        }else{
            maxes.push_back(max);
        }
    }
    return maxes;
}

```cpp
#include <vector>
#include <algorithm>
using namespace std;

vector<int> rolling_max(vector<int> numbers){
    vector<int> maxes;
    int max = INT_MIN;
    for(int i=0; i<numbers.size(); i++){
        if(numbers[i] > max){
            max = numbers[i];
            maxes.push_back(max);
        }else{
            maxes.push_back(max);
        }
    }
    return maxes;
}
```
