    int res = 0;
    for(int i = 0; i < operato.size(); i++){
        string op = operato[i];
        int num = operand[i];
        if(i == 0)
            res = num;
        else{
            if(op == "+"){
                res += num;
            }
            if(op == "-"){
                res -= num;
            }
            if(op == "*"){
                res *= num;
            }
            if(op == "/"){
                res /= num;
            }
            if(op == "%"){
                res %= num;
            }
            if(op == "**"){
                res = pow(res, num);
            }
            if(op == "//"){
                res = res/num;
            }
            if(op == "<<"){
                res = res<<num;
            }
            if(op == ">>"){
                res = res>>num;
            }
        }
    }
    return res;
}
int main(){
    vector<string> op = {"+", "*", "-"};
    vector<int> num = {2, 3, 4, 5};
    printf("%d\n", do_algebra(op, num));
    return 0;
}
