
The problem is asking to find the sum of all the odd numbers in the vector that are at even positions. For example, in the vector {5, 8, 7, 1}, the odd numbers at even positions are 5 and 7, and their sum is 12.

Here is the solution in C++:
```
#include <vector>
#include <iostream>

int solution(std::vector<int> lst) {
    int sum = 0;
    for (int i = 0; i < lst.size(); i++) {
        if (i % 2 == 0 && lst[i] % 2 != 0) {
            sum += lst[i];
        }
    }
    return sum;
}

int main() {
    std::vector<int> lst = {5, 8, 7, 1};
    std::cout << solution(lst) << std::endl;
    return 0;
}
```
This code uses a loop to iterate over the vector. For each element, it checks if the position is even (i % 2 == 0) and if the element is odd (lst[i] % 2 != 0). If both conditions are true, it adds the element to the sum. Finally, it returns the sum.

You can run this code and it will print 12, which is the sum of the odd numbers at even positions in the vector {5, 8, 7, 1}.