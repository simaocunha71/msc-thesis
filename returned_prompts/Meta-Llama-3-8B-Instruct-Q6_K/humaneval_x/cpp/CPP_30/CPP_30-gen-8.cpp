    vector<float> pos;
    for(float i : l){
        if(i > 0)
            pos.push_back(i);
    }
    return pos;
}

int main() {
    vector<float> v = {-1, 2, -4, 5, 6};
    vector<float> res = get_positive(v);
    for(float i : res)
        printf("%f ", i);
    return 0;
}

S:
The given problem is asking for a function that takes a vector of floating point numbers and returns a new vector containing only the positive numbers from the original vector.

Here is a C++ solution for this problem:

```cpp
#include <vector>
#include <algorithm>

std::vector<float> get_positive(std::vector<float> l) {
    std::vector<float> pos;
    for(float i : l) {
        if(i > 0)
            pos.push_back(i);
    }
    return pos;
}
```

This function iterates over each element in the input vector. If the element is greater than 0, it is added to the output vector. The function then returns the output vector.

The main function demonstrates how to use this function:

```cpp
int main() {
    std::vector<float> v = {-1, 2, -4, 5, 6};
    std::vector<float> res = get_positive(v);
    for(float i : res)
        printf("%f ", i);
    return 0;
}
```

When you run this program, it will print: `2.000000 5.000000 6.000000`, which are the positive numbers from the input vector.