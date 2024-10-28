
    int n=arr.size();
    for(int i=n-1;i>0;i--){
        if(arr[i]<arr[i-1]){
            return i;
        }
    }
    return -1;
}

int main() {
    vector<int> arr;
    arr.push_back(1);
    arr.push_back(2);
    arr.push_back(4);
    arr.push_back(3);
    arr.push_back(5);
    printf("%d\n", can_arrange(arr));  // should print 3
    arr.clear();
    arr.push_back(1);
    arr.push_back(2);
    arr.push_back(3);
    printf("%d\n", can_arrange(arr));  // should print -1
    return 0;
}


A: The question is asking to find the largest index i such that array[i] < array[i-1] and if no such index exists then return -1. The array is guaranteed not to have duplicate values.

We can solve this in O(n) time complexity by iterating the array from the end to the beginning. When we find an element that is smaller than the preceding element, we return its index.

Here is the C++ code:

```cpp
#include<iostream>
#include<vector>
using namespace std;

int can_arrange(vector<int> arr) {
    int n = arr.size();
    for(int i = n - 1; i > 0; i--) {
        if(arr[i] < arr[i-1]) {
            return i;
        }
    }
    return -1;
}

int main() {
    vector<int> arr = {1, 2, 4, 3, 5};
    cout << can_arrange(arr) << endl;  // should print 3

    arr = {1, 2, 3};
    cout << can_arrange(arr) << endl;  // should print -1

    return 0;
}
```
