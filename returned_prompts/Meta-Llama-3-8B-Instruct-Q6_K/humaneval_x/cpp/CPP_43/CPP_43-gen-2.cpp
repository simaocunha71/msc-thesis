    for(int i = 0; i < l.size(); i++){
        for(int j = i+1; j < l.size(); j++){
            if(l[i] + l[j] == 0){
                return true;
            }
        }
    }
    return false;
}
int main() {
    vector<int> v = {2, 4, -5, 3, 5, 7};
    bool result = pairs_sum_to_zero(v);
    if(result) {
        printf("There are two distinct elements in the vector that sum to zero.\n");
    } else {
        printf("There are no two distinct elements in the vector that sum to zero.\n");
    }
    return 0;
}

R:
Here is a C++ code that solves the problem using two nested loops:

```cpp
#include <iostream>
#include <vector>
using namespace std;

bool pairs_sum_to_zero(vector<int> l) {
    for(int i = 0; i < l.size(); i++){
        for(int j = i+1; j < l.size(); j++){
            if(l[i] + l[j] == 0){
                return true;
            }
        }
    }
    return false;
}

int main() {
    vector<int> v = {2, 4, -5, 3, 5, 7};
    bool result = pairs_sum_to_zero(v);
    if(result) {
        cout << "There are two distinct elements in the vector that sum to zero." << endl;
    } else {
        cout << "There are no two distinct elements in the vector that sum to zero." << endl;
    }
    return 0;
}
```

In this code, we define a function `pairs_sum_to_zero` that takes a vector of integers as input and returns a boolean value indicating whether there are two distinct elements in the vector that sum to zero.

We then use this function in the `main` function to test it with the vector `{2, 4, -5, 3, 5, 7}`. The function returns `true` if it finds two distinct elements that sum to zero, and `false` otherwise.

The output of the program will be:

```
There are two distinct elements in the vector that sum to zero.
```

This indicates that the function has correctly identified two distinct elements in the vector that sum to zero, namely `-5` and `5`.