    sort(l.begin(), l.end());
    if(l.size() % 2 == 0) {
        float median1 = l[l.size()/2 - 1];
        float median2 = l[l.size()/2];
        return (median1 + median2) / 2;
    } else {
        return l[l.size()/2];
    }
}
int main() {
    vector<float> l = {3, 1, 2, 4, 5};
    printf("%.1f\n", median(l));
    vector<float> l2 = {-10, 4, 6, 1000, 10, 20};
    printf("%.1f\n", median(l2));
    return 0;
}

S:
The median of a list of numbers is the middle value when the list is sorted in ascending order. If the list has an even number of elements, the median is the average of the two middle values.

The median function in this problem takes a vector of floats as input, sorts the vector, and then calculates the median.

Here is the solution:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

float median(std::vector<float> l) {
    std::sort(l.begin(), l.end());

    if (l.size() % 2 == 0) {
        return (l[l.size()/2 - 1] + l[l.size()/2]) / 2.0;
    } else {
        return l[l.size()/2];
    }
}

int main() {
    std::vector<float> l = {3, 1, 2, 4, 5};
    std::cout << median(l) << std::endl;

    std::vector<float> l2 = {-10, 4, 6, 1000, 10, 20};
    std::cout << median(l2) << std::endl;

    return 0;
}
```
This code sorts the input vector using the `std::sort` function from the `<algorithm>` library. Then, it checks if the size of the vector is even or odd. If the size is even, it calculates the median as the average of the two middle values. If the size is odd, it returns the middle value. Finally, it prints the median of the input vectors.