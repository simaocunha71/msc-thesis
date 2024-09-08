/* 
You can solve this problem by using the stack data structure, but to make it more challenging, 
I ask you to solve it without using a stack. Here is the idea how to solve it:

1. Iterate through the operator vector from the end to the beginning. 
2. When you encounter an operator, perform the operation with the current operator and the 
   two operands from the operand vector. 
3. Remove the last two operands from the operand vector and replace them with the result of 
   the operation. 
4. Continue this process until you reach the beginning of the operator vector. 
5. The result of the operation will be the last remaining operand in the operand vector. 
*/

    int result=0;
    for(int i=operato.size()-1;i>=0;i--){
        if(operato[i]=="+"){
            result = operand[i] + operand[i+1];
            operand.erase(operand.begin()+i,operand.begin()+i+2);
            operand.insert(operand.begin()+i,result);
        }
        else if(operato[i]=="-"){
            result = operand[i] - operand[i+1];
            operand.erase(operand.begin()+i,operand.begin()+i+2);
            operand.insert(operand.begin()+i,result);
        }
        else if(operato[i]=="*"){
            result = operand[i] * operand[i+1];
            operand.erase(operand.begin()+i,operand.begin()+i+2);
            operand.insert(operand.begin()+i,result);
        }
        else if(operato[i]=="//"){
            result = operand[i] // operand[i+1];
            operand.erase(operand.begin()+i,operand.begin()+i+2);
            operand.insert(operand.begin()+i,result);
        }
        else if(operato[i]=="**"){
            result = pow(operand[i], operand[i+1]);
            operand.erase(operand.begin()+i,operand.begin()+i+2);
            operand.insert(operand.begin()+i,result);
        }
        else{
            printf("Invalid operator\n");
            return -1;
        }
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
请问以上代码有什么问题？

这段代码