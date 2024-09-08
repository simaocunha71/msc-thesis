    int res = 0;
    int i = 0;
    int j = 0;
    string temp = "";
    while(i < operato.size()){
        temp = operato[i];
        j = i + 1;
        while(j < operato.size() && operato[j] != "+"){
            temp += operato[j];
            j++;
        }
        int a = 0;
        int b = 0;
        if(temp == "*"){
            a = operand[i];
            b = operand[i+1];
            res = a * b;
        }
        else if(temp == "+"){
            a = operand[i];
            b = operand[i+1];
            res = a + b;
        }
        else if(temp == "-"){
            a = operand[i];
            b = operand[i+1];
            res = a - b;
        }
        else if(temp == "//"){
            a = operand[i];
            b = operand[i+1];
            res = a / b;
        }
        else if(temp == "**"){
            a = operand[i];
            b = operand[i+1];
            res = pow(a,b);
        }
        i = j;
    }
    return res;
}
int main()
{
    vector<string> op={"+", "*", "-"};
    vector<int> opd={2, 3, 4, 5};
    int result = do_algebra(op, opd);
    printf("%d",result);
    return 0;
} 

B:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int do_algebra(vector<string>& operato, vector<int>& operand) {
    int res = 0;
    int i = 0;
    int j = 0;
    string temp = "";
    while (i < operato.size()) {
        temp = operato[i];
        j = i + 1;
        while (j < operato.size() && operato[j] != "+") {
            temp += operato[j];
            j++;
        }
        int a = 0;
        int b = 0;
        if (temp == "*") {
            a = operand[i];
            b = operand[i + 1];
            res = a * b;
        } else if (temp == "+") {
            a = operand[i];
            b = operand[i + 1];
            res = a + b;
        } else if (temp == "-") {
           