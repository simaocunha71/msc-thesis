    int a = operand[0];
    for(int i = 0; i < operato.size(); i++){
        if(operato[i] == "+"){
            a = a + operand[i + 1];
            goto A;
        }else if(operato[i] == "-"){
            a = a - operand[i + 1];
            goto A;
        }else if(operato[i] == "*"){
            a = a * operand[i + 1];
            goto A;
        }else if(operato[i] == "//"){
            a = a // operand[i + 1];
            goto A;
        }else if(operato[i] == "**"){
            a = pow(a, operand[i + 1]);
            goto A;
        }
    }
    return a;
}
int main(){
    vector<string> op;
    vector<int> opnd;
    string s;
    while(scanf("%s", &s) != EOF){
        op.push_back(s);
        int tmp;
        scanf("%d", &tmp);
        opnd.push_back(tmp);
    }
    printf("%d\n", do_algebra(op, opnd));
    return 0;
}

*/


































































































































































































