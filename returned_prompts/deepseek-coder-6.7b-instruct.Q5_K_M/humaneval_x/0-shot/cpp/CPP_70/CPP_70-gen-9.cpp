    sort(lst.begin(), lst.end());
    vector<int> result;

    while(!lst.empty()){
        result.push_back(lst.front());
        lst.erase(lst.begin());
        if(!lst.empty()){
            result.push_back(lst.back());
            lst.pop_back();
        }
    }
    return result;
}
*/


A: Here is the C++ code that solves the problem:

```cpp
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> strange_sort_vector(vector<int> nums){
    sort(nums.begin(), nums.end());
    vector<int> result;

    while(!nums.empty()){
        result.push_back(nums.front());
        nums.erase(nums.begin());
        if(!nums.empty()){
            result.push_back(nums.back());
            nums.pop_back();
        }
    }
    return result;
}

int main() {
    vector<int> vec = {1, 2, 3, 4};
    vector<int> result = strange_sort_vector(vec);
    for(int i=0; i<result.size(); i++)
        cout << result[i] << " ";
    return 0;
}
```
This C++ code uses the STL sort function to sort the input vector in ascending order. Then it uses a while loop to alternate between the front and back elements of the vector and push them into a new vector. It continues this until the original vector is empty. The function returns the new vector.
The main function tests the function with the vector {1, 2, 3, 4} and prints the result.

The complexity of this solution is O(n log n) due to sorting, where n is the size of the input vector.




































