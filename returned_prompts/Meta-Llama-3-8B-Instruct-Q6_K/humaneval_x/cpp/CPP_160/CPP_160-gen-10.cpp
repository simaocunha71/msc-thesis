    int len = operato.size();
    if(len<1||len>operand.size()-1){
        return -1;
    }
    int i=0;
    int res=operand[0];
    while(i<len){
        if(operato[i] == "+"){
            res += operand[i+1];
        }
        else if(operato[i] == "-"){
            res -= operand[i+1];
        }
        else if(operato[i] == "*"){
            res *= operand[i+1];
        }
        else if(operato[i] == "//"){
            res = res / operand[i+1];
        }
        else if(operato[i] == "**"){
            res = pow(res, operand[i+1]);
        }
        i++;
    }
    return res;

}

int main(){
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    int result = do_algebra(operato, operand);
    printf("%d", result);
    return 0;
}

