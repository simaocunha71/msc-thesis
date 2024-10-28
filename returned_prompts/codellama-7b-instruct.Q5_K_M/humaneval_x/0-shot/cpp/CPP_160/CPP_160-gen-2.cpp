    int i = 0;
    int j = 0;
    int result = 0;
    while(i < operato.size() && j < operand.size()){
        if(operato[i] == "+"){
            result += operand[j];
            j++;
            i++;
        }else if(operato[i] == "-"){
            result -= operand[j];
            j++;
            i++;
        }else if(operato[i] == "*"){
            result *= operand[j];
            j++;
            i++;
        }else if(operato[i] == "/"){
            result /= operand[j];
            j++;
            i++;
        }else if(operato[i] == "%"){
            result %= operand[j];
            j++;
            i++;
        }else if(operato[i] == "^"){
            result = pow(result, operand[j]);
            j++;
            i++;
        }else if(operato[i] == "//"){
            result = floor(result/operand[j]);
            j++;
            i++;
        }else if(operato[i] == "!"){
            result = fact(result);
            i++;
        }
        else{
            result = operand[j];
            j++;
            i++;
        }
    }
    return result;
}

int fact(int n){
    int result = 1;
    for(int i = 1; i <= n; i++){
        result *= i;
    }
    return result;
}
int main(){
    vector<string> operator{"+", "*", "-"};
    vector<int> operand{2, 3, 4, 5};
    int result = do_algebra(operator, operand);
    printf("%d", result);
    return 0;
}
