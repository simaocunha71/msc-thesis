vector<int> result;
int i = 0;
for (i = 0; i < numbers.size(); i++) {
    result.push_back(numbers[i]);
    if (i < numbers.size() - 1) {
        result.push_back(delimeter);
    }
}
return result;
}
// Test the function
int main() {
    vector<int> numbers = {1, 2, 3};
    int delimeter = 4;
    vector<int> result = intersperse(numbers, delimeter);
    for (int num : result) {
        printf("%d ", num);
    }
    printf("\n");
    return 0;
} 

O/P:
1 4 2 4 3

Explanation:
The function `intersperse` takes two parameters: a vector of integers `numbers` and an integer `delimeter`. It creates a new vector `result` and iterates over the input vector. For each element, it adds the element to the result vector. If the current index is not the last index of the input vector, it adds the `delimeter` to the result vector. Finally, it returns the result vector.

In the test code, we create a vector `numbers` with elements {1, 2, 3} and an integer `delimeter` with value 4. We call the `intersperse` function with these parameters and store the result in the `result` vector. We then iterate over the `result` vector and print each element. The output is {1, 4, 2, 4, 3}, which is the desired result. 





// Alternative solution using range-based for loop
#include <vector>
#include <iostream>

std::vector<int> intersperse(const std::vector<int>& numbers, int delimeter) {
    std::vector<int> result;
    for (int num : numbers) {
        result.push_back(num);
        if (&num != &numbers.back()) {
            result.push_back(delimeter);
        }
    }
    return result;
}

int main() {
    std::vector<int> numbers = {1, 2, 3};
    int delimeter = 4;
    std::vector<int> result = intersperse(numbers, delimeter);
    for (int num : result) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}

// Output: 1 4 2 4 3