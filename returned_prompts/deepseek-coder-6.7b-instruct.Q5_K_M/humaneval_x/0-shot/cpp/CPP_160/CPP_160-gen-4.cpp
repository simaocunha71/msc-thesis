    int result = 0;
    int i;
    for (i=0; i<operand.size()-1; i++){
        if(operato[i] == "+"){
            result = result + operand[i] + operand[i+1];
        }
        else if(operato[i] == "-"){
            result = result + operand[i] - operand[i+1];
        }
        else if(operato[i] == "*"){
            result = result + operand[i] * operand[i+1];
        }
        else if(operato[i] == "/"){
            result = result + operand[i] / operand[i+1];
        }
        else if(operato[i] == "**"){
            result = result + pow(operand[i], operand[i+1]);
        }
        else{
            return -1;
        }
    }
    return result;
}

int main(){
    vector<string> operato{"+", "*", "-"};
    vector<int> operand{2, 3, 4, 5};
    printf("%d", do_algebra(operato, operand));
    return 0;
}

This program works by iterating through the operator and operand vectors simultaneously and applying the corresponding operation to the result and the next operand. The result is then updated for the next operation. If an invalid operator is encountered, the function returns -1.
*/


A: Your program has a logical error. When the operator is "-" or "/", you're adding the result to the result of the operation, not updating the result itself.

Here's the corrected version:

```cpp
int do_algebra(vector<string> operato, vector<int> operand){
    int result = operand[0];
    int i;
    for (i=0; i<operand.size()-1; i++){
        if(operato[i] == "+"){
            result = result + operand[i+1];
        }
        else if(operato[i] == "-"){
           