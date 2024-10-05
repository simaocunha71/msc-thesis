    int res = operato[0];
    int i = 1;
    while(i<operato.size()){
        if(operato[i]=="+"){
            res+=operand[i];
        }else if(operato[i]=="-"){
            res-=operand[i];
        }else if(operato[i]=="*"){
            res*=operand[i];
        }else if(operato[i]=="//"){
            res/=operand[i];
        }else if(operato[i]=="**"){
            res=pow(res, operand[i]);
        }
        i++;
    }
    return res;
}

int main(){
    vector<string> operato;
    vector<int> operand;
    char a;
    int b;
    do{
        scanf("%c", &a);
        operato.push_back(a);
    }while(a!='.');
    operato.pop_back();
    scanf("%d", &b);
    operand.push_back(b);
    while(scanf("%d", &b)!=EOF){
        operand.push_back(b);
    }
    printf("%d\n", do_algebra(operato, operand));
}



*/





























































































































































































