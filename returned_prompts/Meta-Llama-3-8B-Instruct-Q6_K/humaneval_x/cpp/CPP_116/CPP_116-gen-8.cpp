    vector<int> result;
    for(int i=0; i<arr.size(); i++){
        int count = 0;
        int num = arr[i];
        while(num > 0){
            if(num & 1)
                count++;
            num >>= 1;
        }
        result.push_back(make_pair(count, arr[i]));
    }
    sort(result.begin(), result.end());
    vector<int> res;
    for(int i=0; i<result.size(); i++){
        res.push_back(result[i].second);
    }
    return res;
}  // your code here

int main()
{
    vector<int> v = {1, 5, 2, 3, 4};
    vector<int> v2 = sort_array(v);
    for(int i=0; i<v2.size(); i++){
        cout<<v2[i]<<" ";
    }
    return 0;
}

Solution:
The problem is to sort a vector of non-negative integers based on the number of ones in their binary representation in ascending order. If two numbers have the same number of ones in their binary representation, then they should be sorted based on their decimal value in ascending order.

Here is the solution in C++:
```cpp
#include <vector>
#include <algorithm>
#include <utility>
#include <iostream>

using namespace std;

vector<int> sort_array(vector<int> arr) {
    vector<pair<int, int>> result;
    for (int i = 0; i < arr.size(); i++) {
        int count = 0;
        int num = arr[i];
        while (num > 0) {
            if (num & 1)
                count++;
            num >>= 1;
        }
        result.push_back(make_pair(count, arr[i]));
    }
    sort(result.begin(), result.end());
    vector<int> res;
    for (int i = 0; i < result.size(); i++) {
        res.push_back(result[i].second);
    }
    return res;
}

int main() {
    vector<int> v = {1, 5, 2, 3, 4};
    vector<int> v2 = sort_array(v);
    for (int i = 0; i < v2.size(); i++) {
        cout << v2[i] << " ";
    }
    return 0;
}
```
This program first creates a new vector `result` where each element is a pair containing the number of ones in the binary representation