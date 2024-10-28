    int len=operato.size();
    if (len==0)
    return 0;
    int i=0;
    int result=operand[i];
    i++;
    for (;i<len;i++)
    {
        if (operato[i]=="+")
        result+=operand[i];
        if (operato[i]=="-")
        result-=operand[i];
        if (operato[i]=="*")
        result*=operand[i];
        if (operato[i]=="/")
        result/=operand[i];
        if (operato[i]=="%")
        result%=operand[i];
        if (operato[i]=="//")
        result=int(result/operand[i]);
        if (operato[i]=="**")
        result=pow(result, operand[i]);
    }
    return result;
}


