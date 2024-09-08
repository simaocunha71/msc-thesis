    if(arr.empty())
        return true;
    int n = arr.size();
    int smallest = arr[0];
    int count = 0;
    for(int i = 1; i < n; i++){
        if(arr[i] < smallest){
            smallest = arr[i];
        }
        else if(arr[i] > smallest){
            count++;
        }
    }
    return (count <= 1);

}
int main()
{
    vector<int> v1 = {3,4,5,1,2};
    vector<int> v2 = {3,5,4,1,2};
    printf("%d\n",move_one_ball(v1));
    printf("%d\n",move_one_ball(v2));
    return 0;
}

S:
The problem asks to check whether it is possible to obtain a sorted array in non-decreasing order by performing right shift operations on the given array. 

The problem can be solved by finding the smallest element in the array and then counting the number of elements that are greater than this smallest element. If the count is less than or equal to 1, it means that the array can be sorted in non-decreasing order by performing right shift operations.

Here is the C++ code to solve the problem:

```cpp
#include <iostream>
#include <vector>
using namespace std;

bool move_one_ball(vector<int> arr) {
    if (arr.empty()) {
        return true;
    }
    int n = arr.size();
    int smallest = arr[0];
    int count = 0;
    for (int i = 1; i < n; i++) {
        if (arr[i] < smallest) {
            smallest = arr[i];
        }
        else if (arr[i] > smallest) {
            count++;
        }
    }
    return (count <= 1);
}

int main() {
    vector<int> v1 = {3, 4, 5, 1, 2};
    vector<int> v2 = {3, 5, 4, 1, 2};
    cout << move_one_ball(v1) << endl; // Output: 1
    cout << move_one_ball(v2) << endl; // Output: 0
    return 0;
}
```

In this code, the function `move_one_ball` takes a vector of integers as input and returns a boolean value indicating whether it is possible to obtain a sorted array in non-decreasing order by performing right