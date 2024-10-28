    int result=operand[0];
    int i;
    for (i=1;i<operato.size();i++){
        if (operato[i]=="+")
        result+=operand[i];
        if (operato[i]=="-")
        result-=operand[i];
        if (operato[i]=="*")
        result*=operand[i];
        if (operato[i]=="/")
        result/=operand[i];
        if (operato[i]=="**")
        result=result*pow(operand[i], 2);
    }
    return result;
}



