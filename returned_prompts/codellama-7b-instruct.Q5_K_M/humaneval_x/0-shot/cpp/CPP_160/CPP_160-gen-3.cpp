    int n = operato.size();
    int m = operand.size();
    if(n == 0 || m == 0){
        return 0;
    }
    if(n == 1){
        int res = operand[0];
        for(int i = 1; i < m; ++i){
            if(operato[0] == "+"){
                res += operand[i];
            }else if(operato[0] == "-"){
                res -= operand[i];
            }else if(operato[0] == "*"){
                res *= operand[i];
            }else if(operato[0] == "/"){
                res /= operand[i];
            }else if(operato[0] == "%"){
                res %= operand[i];
            }else{
                goto A;
            }
        }
        return res;
    }
    int res = do_algebra(vector<string>(operato.begin(), operato.begin()+n-1), vector<int>(operand.begin(), operand.begin()+n-1));
    if(operato[n-1] == "+"){
        res += operand[n-1];
    }else if(operato[n-1] == "-"){
        res -= operand[n-1];
    }else if(operato[n-1] == "*"){
        res *= operand[n-1];
    }else if(operato[n-1] == "/"){
        res /= operand[n-1];
    }else if(operato[n-1] == "%"){
        res %= operand[n-1];
    }else{
        goto A;
    }
    return res;
}
int main(){
    vector<string> operator = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    int res = do_algebra(operator, operand);
    printf("%d\n", res);
    return 0;
}
