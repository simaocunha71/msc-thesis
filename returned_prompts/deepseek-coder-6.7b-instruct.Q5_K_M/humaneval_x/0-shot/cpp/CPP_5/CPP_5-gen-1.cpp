vector<int> intersperse(vector<int> numbers, int delimeter){ 

    vector<int> result;
    for(int i=0; i<numbers.size(); i++){
        result.push_back(numbers[i]);
        if(i != numbers.size() - 1)
            result.push_back(delimeter);
    }
    return result;
}

*/

int main() {
    vector<int> numbers = {1, 2, 3};
    int delimeter = 4;
    vector<int> result = intersperse(numbers, delimeter);
    for(int i=0; i<result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}
```

## C++ version (C++11 and above)

```cpp
#include <iostream>
#include <vector>

std::vector<int> intersperse(const std::vector<int>& numbers, int delimeter){ 
    std::vector<int> result;
    for(size_t i=0; i<numbers.size(); i++){
        result.push_back(numbers[i]);
        if(i != numbers.size() - 1)
            result.push_back(delimeter);
    }
    return result;
}

int main() {
    std::vector<int> numbers = {1, 2, 3};
    int delimeter = 4;
    std::vector<int> result = intersperse(numbers, delimeter);
    for(int num : result){
        std::cout << num << " ";
    }
    return 0;
}
```

## Python version

```python
def intersperse