    int n = arr.size();
    int count = 0;
    for(int i=0; i<n/2; i++){
        if(arr[i] != arr[n-i-1]){
            count++;
        }
    }
    return count;
}
*/

#include <stdio.h>
#include <vector>
using namespace std;

int smallest_change(vector<int> arr){
    int n = arr.size();
    int count = 0;

    for(int i = 0; i < n/2; i++){
        if(arr[i] != arr[n-i-1]){
            count++;
        }
    }
    return count;
}

int main() {
    vector<int> arr = {1, 2, 3, 2, 1};
    printf("%d\n", smallest_change(arr));
    return 0;
}
```

Here is the C++ solution:

```cpp
#include <iostream>
#include <vector>
using namespace std;

int smallest_change(vector<int> arr){
    int n = arr.size();
    int count = 0;

    for(int i = 0; i < n/2; i++){
        if(arr[i] != arr[n-i-1]){
            count++;
        }
    }
    return count;
}

int main() {
    vector<int> arr = {1, 2, 3, 2, 1};
    cout << smallest_change(arr) << endl;
    return 0;
}
```

This solution works by iterating through the first half of the array and comparing each element to its corresponding element from the end of the array. If they are not equal, it increments a counter. The function then returns this counter, which represents the minimum number of changes required to make the array palindromic.

The time complexity of this solution is O(n/2), where n is the length of the array, since it only needs to iterate through half of the array. The space complexity is O(1),