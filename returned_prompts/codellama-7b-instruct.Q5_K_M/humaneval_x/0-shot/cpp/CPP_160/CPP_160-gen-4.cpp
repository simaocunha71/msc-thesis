    for(int i = 0; i < operato.size(); i++){
        if(operato[i] == "+"){
            return operand[i] + operand[i+1];
        }
        else if(operato[i] == "-"){
            return operand[i] - operand[i+1];
        }
        else if(operato[i] == "*"){
            return operand[i] * operand[i+1];
        }
        else if(operato[i] == "/"){
            return operand[i] / operand[i+1];
        }
        else if(operato[i] == "%"){
            return operand[i] % operand[i+1];
        }
        else if(operato[i] == "^"){
            return pow(operand[i], operand[i+1]);
        }
        else if(operato[i] == "//"){
            return (int)(operand[i] / operand[i+1]);
        }
    }
}

int main(){
    vector<string> op;
    vector<int> operand;
    int a;
    string str;
    while(cin >> str){
        if(str == "//"){
            op.push_back("//");
        }
        else if(str == "^"){
            op.push_back("^");
        }
        else if(str == "*"){
            op.push_back("*");
        }
        else if(str == "+"){
            op.push_back("+");
        }
        else if(str == "-"){
            op.push_back("-");
        }
        else if(str == "/"){
            op.push_back("/");
        }
        else if(str == "%"){
            op.push_back("%");
        }
        else{
            a = atoi(str.c_str());
            operand.push_back(a);
        }
    }
    int result = do_algebra(op, operand);
    printf("%d\n