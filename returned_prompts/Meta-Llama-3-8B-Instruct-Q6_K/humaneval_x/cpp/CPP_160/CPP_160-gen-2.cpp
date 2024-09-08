    int n = operato.size();
    int m = operand.size();
    if(n+1!=m){
        printf("Error: The length of operator vector is not equal to the length of operand vector minus one.\n");
        return -1;
    }
    if(m<2){
        printf("Error: The operand vector has less than two operands.\n");
        return -1;
    }
    for(int i = 0; i<n; i++){
        if(operato[i]!="+" && operato[i]!="-" && operato[i]!="*" && operato[i]!="//" && operato[i]!="**"){
            printf("Error: The operator vector has an invalid operator.\n");
            return -1;
        }
    }
    for(int i = 0; i<m; i++){
        if(operand[i]<0){
            printf("Error: The operand vector has a negative integer.\n");
            return -1;
        }
    }
    double res = operand[0];
    for(int i = 0; i<n; i++){
        double num = 0;
        switch(operato[i].at(0)){
            case '+':
                num = res + operand[i+1];
                break;
            case '-':
                num = res - operand[i+1];
                break;
            case '*':
                num = res * operand[i+1];
                break;
            case '/':
                num = res / operand[i+1];
                break;
            case '^':
                num = pow(res, operand[i+1]);
                break;
        }
        res = num;
    }
    return (int)res;
}

int main()
{
    vector<string> operator={"+", "*", "-"};
    vector<int> operand={2, 3, 4, 5};
    int result = do_algebra(operator, operand);
    if(result != -1)
        printf("Result: %d\n", result);
    return 0;
}

B:
    int do_algebra(vector<string> operato, vector<int> operand){
        if(operato.size() + 1 != operand.size()){
            return -1;
        }
        if(operand.size() < 2){
            return -1;
        }
        for(int i = 0; i<operato.size(); i++){
            if(operato[i] != "+" && operato[i] != "-" && operato[i] != "*" && operato[i]