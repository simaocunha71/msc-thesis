/*
Given two vectors operator, and operand. The first vector has basic algebra operations, and 
the second vector is a vector of integers. Use the two given vectors to build the algebric 
expression and return the evaluation of this expression.

The basic algebra operations:
Addition ( + ) 
Subtraction ( - ) 
Multiplication ( * ) 
Floor division ( // ) 
Exponentiation ( ** ) 

Example:
operator{"+", "*", "-"}
vector = {2, 3, 4, 5}
result = 2 + 3 * 4 - 5
=> result = 9

Note:
    The length of operator vector is equal to the length of operand vector minus one.
    Operand is a vector of of non-negative integers.
    Operator vector has at least one operator, and operand vector has at least two operands.

*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;
#include<algorithm>
#include<stdlib.h>
int do_algebra(vector<string> operato, vector<int> operand){
    int result = 0;
    for(int i = 0; i < operato.size(); i++){
        if(operato[i] == "+"){
            result = operand[i] + operand[i+1];
        }
        else if(operato[i] == "-"){
            result = operand[i] - operand[i+1];
        }
        else if(operato[i] == "*"){
            result = operand[i] * operand[i+1];
        }
        else if(operato[i] == "/"){
            result = operand[i] / operand[i+1];
        }
        else if(operato[i] == "**"){
            result = pow(operand[i], operand[i+1]);
        }
        else{
            printf("Error: Unknown operator.\n");
            exit(1);
        }
        operand[i+1] = result;
    }
    return result;
}
int main(){
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    int result = do_algebra(operato, operand);
    printf("Result: %d\n", result);
    return 0;
}