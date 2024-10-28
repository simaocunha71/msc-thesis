    int i,j;
    int result=0;
    for (i=0;i<operato.size();i++){
        if (operato[i]=="+")
        result+=operand[i];
        if (operato[i]=="*")
        result*=operand[i];
        if (operato[i]=="/")
        result/=operand[i];
        if (operato[i]=="-")
        result-=operand[i];
        if (operato[i]=="^")
        result=pow(result,operand[i]);
    }
    return result;
}



