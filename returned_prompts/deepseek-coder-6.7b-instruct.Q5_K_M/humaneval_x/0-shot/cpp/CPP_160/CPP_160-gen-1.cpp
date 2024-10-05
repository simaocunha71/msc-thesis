    int res = operand[0];
    for (int i = 1; i < operand.size(); i++){
        switch (operato[i - 1][0]){
            case '+':
                res += operand[i];
                break;
            case '-':
                res -= operand[i];
                break;
            case '*':
                res *= operand[i];
                break;
            case '/':
                res /= operand[i];
                break;
            case '^':
                res = pow(res, operand[i]);
                break;
        }
    }
    return res;
}
int main(){
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    printf("%d", do_algebra(operato, operand));
    return 0;
}

*/


A: Your code seems to be correct, but it lacks the main function. In C++, you need to put everything inside a main function to run the program. Here is the complete code:

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int do_algebra(vector<string> operato, vector<int> operand){
    int res = operand[0];
    for (int i = 1; i < operand.size(); i++){
        switch (operato[i - 1][0]){
            case '+':
                res += operand[i];
                break;
            case '-':
                res -= operand[i];
                break;
            case '*':
                res *= operand[i];
                break;
            case '/':
                res /= operand[i];
                break;
            case '^':
                res = pow(res, operand[i]);
                break;
        }
    }
    return res;
}

int main(){
    vector<string> operato = {"+", "*", "-"};
    vector<int