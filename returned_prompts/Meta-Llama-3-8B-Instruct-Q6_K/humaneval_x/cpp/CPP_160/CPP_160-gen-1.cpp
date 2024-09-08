    int i, j, k, n;
    n = operato.size();
    j = 0;
    for(i = 0; i < n; i++) {
        if(operato[i] == "+") {
            k = j;
            j++;
            j = j + operand[k];
        } else if(operato[i] == "-") {
            k = j;
            j++;
            j = j - operand[k];
        } else if(operato[i] == "*") {
            k = j;
            j++;
            j = j * operand[k];
        } else if(operato[i] == "//") {
            k = j;
            j++;
            j = j // operand[k];
        } else if(operato[i] == "**") {
            k = j;
            j++;
            j = pow(j, operand[k]);
        }
    }
    return j;
}
int main() {
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    printf("%d\n", do_algebra(operato, operand));
    return 0;
}

// Corrected code
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int do_algebra(vector<string> operator_, vector<int> operand_) {
    int result = operand_[0];
    for (int i = 0; i < operator_.size(); i++) {
        if (operator_[i] == "+") {
            result += operand_[i + 1];
        } else if (operator_[i] == "-") {
            result -= operand_[i + 1];
        } else if (operator_[i] == "*") {
            result *= operand_[i + 1];
        } else if (operator_[i] == "//") {
            result /= operand_[i + 1];
        } else if (operator_[i] == "**") {
            result = pow(result, operand_[i + 1]);
        }
    }
    return result;
}

int main() {
    vector<string> operator_ = {"+", "*", "-"};
    vector<int> operand_ = {2, 3, 4, 5};
    cout << do_algebra(operator_, operand_) << endl;
    return 0;
}

// Explanation:
// The corrected code is written in C++ and it uses a vector of strings and a vector