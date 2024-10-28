    int result=0;
    int i;
    for (i=0;i<operato.size();i++)
    {
        if (operato[i]=="+")
        result+=operand[i+1];
        if (operato[i]=="-")
        result-=operand[i+1];
        if (operato[i]=="*")
        result*=operand[i+1];
        if (operato[i]=="**")
        result=result^operand[i+1];
        if (operato[i]=="//")
        result=result/operand[i+1];

    }
    return result;
}