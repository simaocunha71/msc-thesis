    int res = operand[0];
    for(int i=0; i<operato.size(); i++){
        if(operato[i] == "+"){
            res += operand[i+1];
        }
        else if(operato[i] == "-"){
            res -= operand[i+1];
        }
        else if(operato[i] == "*"){
            res *= operand[i+1];
        }
        else if(operato[i] == "/"){
            res /= operand[i+1];
        }
        else if(operato[i] == "**"){
            res = pow(res, operand[i+1]);
        }
    }
    return res;
}

int main(){
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    printf("%d\n", do_algebra(operato, operand));
}


A: Your code is almost correct but you have a small typo. 
In the else if condition where you are checking if the operator is "/", you should replace it with "//" as it is the floor division operator in C++. 

Also, you should make sure that the division and floor division operations are not performed on zero to avoid the division by zero runtime error.

Here is the corrected code:

```cpp
#include<iostream>
#include<vector>
#include<string>
#include<cmath>
using namespace std;

int do_algebra(vector<string> operato, vector<int> operand){
    int res = operand[0];
    for(int i=0; i<operato.size(); i++){
        if(operato[i] == "+"){
            res += operand[i+1];
        }
        else if(operato[i] == "-"){
            res -= operand[i+1];
        }
        else if(operato[i] == "*"){
            res *= operand[i+1