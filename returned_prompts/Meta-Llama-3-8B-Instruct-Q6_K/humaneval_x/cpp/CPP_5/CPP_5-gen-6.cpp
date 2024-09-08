    vector<int> result;
    for (int i = 0; i < numbers.size(); i++) {
        result.push_back(numbers[i]);
        if (i < numbers.size() - 1) {
            result.push_back(delimeter);
        }
    }
    return result;
}

int main() {
    vector<int> numbers = {1, 2, 3};
    int delimeter = 4;
    vector<int> result = intersperse(numbers, delimeter);
    for (int i : result) {
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}

C++:
```cpp
#include <vector>
#include <algorithm>
#include <iostream>

std::vector<int> intersperse(const std::vector<int>& numbers, int delimeter) {
    std::vector<int> result;
    result.reserve(numbers.size() + numbers.size() - 1);
    for (int i = 0; i < numbers.size(); i++) {
        result.push_back(numbers[i]);
        if (i < numbers.size() - 1) {
            result.push_back(delimeter);
        }
    }
    return result;
}

int main() {
    std::vector<int> numbers = {1, 2, 3};
    int delimeter = 4;
    std::vector<int> result = intersperse(numbers, delimeter);
    for (int i : result) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

Output:
```
1 4 2 4 3
```

Time complexity: O(n), where n is the size of the input vector `numbers`. 

Space complexity: O(n), where n is the size of the input vector `numbers`. This is because we are creating a new vector to store the result, which can be as large as the input vector. 

Note: The `reserve` function is used to pre-allocate memory for the `result` vector to avoid reallocation and improve performance. 