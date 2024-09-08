
The function `do_algebra` takes two vectors as input, `operato` and `operand`. It iterates through the `operato` vector and performs the corresponding operation on the `operand` vector. The result is returned at the end.

In the main function, we create two vectors, `operato` and `operand`, and call the `do_algebra` function with these vectors as arguments. The result is then printed to the console.

Here is the corrected code:

```c++
#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int do_algebra(vector<string> operato, vector<int> operand) {
    int result = operand[0];
    for (int i = 0; i < operato.size(); i++) {
        if (operato[i] == "+") {
            result += operand[i + 1];
        } else if (operato[i] == "-") {
            result -= operand[i + 1];
        } else if (operato[i] == "*") {
            result *= operand[i + 1];
        } else if (operato[i] == "//") {
            result = result / operand[i + 1];
        } else if (operato[i] == "**") {
            result = pow(result, operand[i + 1]);
        }
    }
    return result;
}

int main() {
    vector<string> operato = {"+", "*", "-"};
    vector<int>