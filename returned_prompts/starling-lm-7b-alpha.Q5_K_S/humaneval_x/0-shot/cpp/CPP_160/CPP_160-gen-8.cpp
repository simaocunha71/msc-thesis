    int i=0;
    int l=operando.size()-1;
    int result=operando[i];
    while(i<l){
        if(operato[i]=="+"){
            result=result+operando[i+1];
            i++;
        }else if(operato[i]=="-"){
            result=result-operando[i+1];
            i++;
        }else if(operato[i]=="*"){
            result=result*operando[i+1];
            i++;
        }else if(operato[i]=="//"){
            result=result//operando[i+1];
            i++;
        }else if(operato[i]=="**"){
            result=pow(result,operando[i+1]);
            i++;
        }else if(i==l){
            printf("%d",result);
            break;
        }
    }
    return result;
}



int main(){
    vector<string> operato;
    vector<int> operando;
    char op[10];
    int n;
    scanf("%s",op);
    operato.push_back(op);
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        int num;
        scanf("%d",&num);
        operando.push_back(num);
    }
    do_algebra(operato,operando);
    return 0;
}














































































































































