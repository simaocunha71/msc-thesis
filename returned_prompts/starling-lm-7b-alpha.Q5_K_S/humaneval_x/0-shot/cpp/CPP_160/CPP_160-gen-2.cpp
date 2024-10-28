    int i = 0;
    int j = 0;
    int k = 0;
    int count = 0;
    int result = 0;
    int x = 0;
    int y = 0;
    int z = 0;
    int q = 0;
    int p = 0;
    int m = 0;
    int n = 0;
    while(i < operato.size()){
        if(operato[i] == "+"){
            result = operand[j] + operand[j + 1];
            j += 2;
            i++;
            continue;
        }else if(operato[i] == "-"){
            result = operand[j] - operand[j + 1];
            j += 2;
            i++;
            continue;
        }else if(operato[i] == "*"){
            result = operand[j] * operand[j + 1];
            j += 2;
            i++;
            continue;
        }else if(operato[i] == "/"){
            result = operand[j] / operand[j + 1];
            j += 2;
            i++;
            continue;
        }else if(operato[i] == "**"){
            result = pow(operand[j], operand[j + 1]);
            j += 2;
            i++;
            continue;
        }
    }
    return result;
}
int main(void){
    vector<string> operato;
    vector<int> operand;
    string a;
    int b;
    int c;
    while(scanf("%s", &a) != EOF){
        operato.push_back(a);
    }
    while(scanf("%d", &b) != EOF){
        operand.push_back(b);
    }
    int result = do_algebra(operato, operand);
    printf("%d\n", result);
    return 0;
}

*/



























