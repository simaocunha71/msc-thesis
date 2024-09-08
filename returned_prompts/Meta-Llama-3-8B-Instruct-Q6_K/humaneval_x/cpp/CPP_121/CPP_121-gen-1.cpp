    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        if(i % 2 == 0 && lst[i] % 2 != 0) {
            sum += lst[i];
        }
    }
    return sum;

}
int main() {
    vector<int> lst = {5, 8, 7, 1};
    printf("Sum of odd elements at even positions: %d\n", solutions(lst));
    return 0;
}

C:
#include <stdio.h>
#include <vector>

int solution(std::vector<int> lst) {
    int sum = 0;
    for(int i = 0; i < lst.size(); i++) {
        if(i % 2 == 0 && lst[i] % 2 != 0) {
            sum += lst[i];
        }
    }
    return sum;
}

int main() {
    std::vector<int> lst = {5, 8, 7, 1};
    printf("Sum of odd elements at even positions: %d\n", solution(lst));
    return 0;
}

P:
```python
def solution(lst):
    return sum([x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 != 0])
```
This function uses a list comprehension to generate a list of odd elements at even positions, and then uses the built-in `sum` function to calculate the sum of this list.

Here's a breakdown of how the function works:

1. `enumerate(lst)`: This function returns a list of tuples, where each tuple contains the index `i` and the value `x` of each element in the list.
2. `if i % 2 == 0 and x % 2 != 0`: This is the condition that filters the list to include only odd elements at even positions.
3. `sum([x for ...])`: This is the sum function, which adds up all the elements in the list.

For example, if the input list is `[5, 8, 7, 1]`, the function will return `12`, which is the sum of the odd elements at even positions (`5` and `7`).