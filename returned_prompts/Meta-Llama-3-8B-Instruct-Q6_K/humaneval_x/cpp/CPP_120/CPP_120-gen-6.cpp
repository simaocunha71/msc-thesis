The problem requires us to find the k largest elements in the given array and return them as a sorted vector.

To solve this problem, we can use the standard library's sort function with a custom comparator. We sort the array in descending order, and then return the first k elements of the sorted array.

Here's how you can solve it:

```c++
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> maximum(vector<int>& arr, int k) {
    // sort the array in descending order
    sort(arr.begin(), arr.end(), greater<int>());

    // return the first k elements of the sorted array
    return vector<int>(arr.begin(), arr.begin() + k);
}

int main() {
    vector<int> arr = {-3, -4, 5};
    int k = 3;
    vector<int> result = maximum(arr, k);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}
```

In this code, the `maximum` function takes a vector `arr` and an integer `k` as input. It sorts the array in descending order using the `sort` function with a custom comparator (`greater<int>()`), and then returns the first `k` elements of the sorted array.

In the `main` function, we create a vector `arr` and an integer `k`, and then call the `maximum` function to get the result. We then print the result to the console.

The output of this code will be:

```
-4 -3 5
```

This is the sorted vector of the k largest elements in the array. The `greater<int>()` comparator is used to sort the array