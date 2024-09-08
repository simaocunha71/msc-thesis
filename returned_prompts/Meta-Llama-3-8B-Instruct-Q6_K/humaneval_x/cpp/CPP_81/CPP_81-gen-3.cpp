    Output:
    A+
    B+
    C-
    C+
    A-

*/



Solution:
This problem can be solved by using a simple if-else statement inside a loop. The function takes a vector of floating-point numbers as input and returns a vector of strings representing the corresponding letter grades. Here is the complete code:

```cpp
#include <iostream>
#include <vector>
#include <string>

std::vector<std::string> numerical_letter_grade(std::vector<float> grades) {
    std::vector<std::string> result;
    for (float grade : grades) {
        if (grade > 4.0) {
            result.push_back("A+");
        }
        else if (grade > 3.7) {
            result.push_back("A");
        }
        else if