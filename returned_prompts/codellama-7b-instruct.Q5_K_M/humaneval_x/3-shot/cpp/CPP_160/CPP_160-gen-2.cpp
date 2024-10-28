    int i;
    int result=operand[0];
    for (i=0;i<operato.size();i++)
    {
        if (operato[i]=="+")
        result+=operand[i+1];
        if (operato[i]=="*")
        result*=operand[i+1];
        if (operato[i]=="/")
        result/=operand[i+1];
        if (operato[i]=="-")
        result-=operand[i+1];
    }
    return result;
}


