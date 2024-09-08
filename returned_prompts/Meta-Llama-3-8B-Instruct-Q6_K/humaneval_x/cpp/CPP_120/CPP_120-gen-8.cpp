    sort(arr.begin(),arr.end());
    vector<int> res;
    for(int i=0;i<k;i++){
        res.push_back(arr[i]);
    }
    return res;
}

int main(){
    vector<int> arr = {-3,-4,5};
    int k = 3;
    vector<int> res = maximum(arr,k);
    for(int i=0;i<res.size();i++){
        printf("%d ",res[i]);
    }
    printf("\n");
    return 0;
}

R:
The task is to return the k largest numbers in the array arr. The solution provided earlier uses the sort function to sort the array in ascending order. However, this approach has a time complexity of O(n log n) due to the sorting operation.

A more efficient approach is to use the partial_sort function, which has a time complexity of O(n log k). This function sorts the first k elements of the array in ascending order.

Here is the modified code:

```cpp
#include <vector>
#include <algorithm>
using namespace std;

vector<int> maximum(vector<int> arr, int k) {
    partial_sort(arr.begin(), arr.begin() + k, arr.end());
    return vector<int>(arr.begin(), arr.begin() + k);
}
```

In this code, the partial_sort function is used to sort the first k elements of the array arr in ascending order. The result is then returned as a new vector.

This approach is more efficient than the previous one, especially for large arrays. However, it still has a time complexity of O(n log k), which may not be suitable for very large arrays.

If you need a solution with a time complexity of O(n log k), you can use the heap data structure. A heap is a binary tree in which each node is smaller than its children. You can use a max heap to store the k largest numbers in the array.

Here is the modified code:

```cpp
#include <vector>
#include <queue>
using namespace std;

vector<int> maximum(vector<int> arr, int k) {
    priority_queue<int> max_heap;
    for (int num : arr) {
        max_heap.push(num);
        if (max_heap.size() > k) {
            max_heap.pop();
        }
    }
    vector<int> res;
    while (max_heap.size()) {
        res.push_back(max_heap.top());
        max_heap.pop();
    }
    return res;
}
```

In this code, a max heap is used to store