    int result = operand[0];
    for(int i=0; i<operato.size(); i++){
        if(operato[i] == "+"){
            result += operand[i+1];
        }
        else if(operato[i] == "-"){
            result -= operand[i+1];
        }
        else if(operato[i] == "*"){
            result *= operand[i+1];
        }
        else if(operato[i] == "//"){
            result /= operand[i+1];
        }
        else if(operato[i] == "**"){
            result = pow(result, operand[i+1]);
        }
    }
    return result;
}

int main(){
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    printf("%d", do_algebra(operato, operand));