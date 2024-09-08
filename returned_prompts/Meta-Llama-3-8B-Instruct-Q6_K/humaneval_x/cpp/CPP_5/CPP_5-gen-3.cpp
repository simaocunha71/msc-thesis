vector<int> result;
for(int i = 0; i < numbers.size(); i++) {
    result.push_back(numbers[i]);
    if(i < numbers.size() - 1) {
        result.push_back(delimeter);
    }
}
return result;
}

C:
def intersperse(numbers, delimeter):
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

Python:
def intersperse(numbers, delimeter):
    return [x for i, x in enumerate(numbers + [delimeter]) if i % 2 == 0]

R:
intersperse <- function(numbers, delimeter) {
  c(numbers, delimeter)[seq(1, length(c(numbers, delimeter)), by = 2)]
}
```
Solution:
Here is a solution in C++:
```c
#include <vector>
using namespace std;

vector<int> intersperse(vector<int> numbers, int delimeter) {
    vector<int> result;
    for (int i = 0; i < numbers.size(); i++) {
        result.push_back(numbers[i]);
        if (i < numbers.size() - 1) {
            result.push_back(delimeter);
        }
    }
    return result;
}
```
Explanation:
This function takes a vector of integers `numbers` and an integer `delimeter` as input. It creates a new vector `result` and iterates over the input vector `numbers`. For each element in `numbers`, it adds the element to `result` and then adds the `delimeter` to `result` if it's not the last element in `numbers`. Finally, it returns the resulting vector.

Here is a solution in Python:
```python
def intersperse(numbers, delimeter):
    return [x for i, x in enumerate(numbers + [delimeter]) if i % 2 == 0]
```
Explanation:
This function takes a list of integers `numbers` and an integer `delimeter` as input. It uses a list comprehension to create a new list `result`. It iterates over the input list `numbers` and adds each element to `result`. It also adds the `delimeter` to `result` after each element, effectively inserting the `delimeter` between each pair of consecutive elements. Finally, it returns the resulting list.

Here is a solution in R:
```R
intersperse <- function(numbers, delimeter