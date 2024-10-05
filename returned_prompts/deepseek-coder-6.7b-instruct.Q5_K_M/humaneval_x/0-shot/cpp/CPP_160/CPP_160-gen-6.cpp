    //Write your solution here
    int result = operand[0];
    for(int i = 1; i < operand.size(); i++){
        if(operato[i-1] == "+"){
            result += operand[i];
        }
        else if(operato[i-1] == "-"){
            result -= operand[i];
        }
        else if(operato[i-1] == "*"){
            result *= operand[i];
        }
        else if(operato[i-1] == "/"){
            result /= operand[i];
        }
        else if(operato[i-1] == "**"){
            result = pow(result, operand[i]);
        }
    }
    return result;
}



int main(){
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    printf("%d\n", do_algebra(operato, operand));
    return 0;
}

*/

This question is a modified version of a question from Leetcode which is a platform that offers coding challenges. The question has been modified to meet the coding standards of this platform.

*/

//Code:

#include<bits/stdc++.h>
using namespace std;

int evalRPN(vector<string> &tokens) {
    stack<int> stk;
    for (string &s : tokens) {
        if (s.size() > 1 || isdigit(s[0])) {
            stk.push(stoi(s));
        } else {
            int op2 = stk.top(); stk.pop();
            int op1 = stk.top(); stk.pop();
            switch (s[0]) {
                case '+':
                    stk.push(op1 + op2);
                    break;
                case '-':
                    stk.push(op1 - op2);
                    break;
                case '*':
                    stk.push(op1 * op2);