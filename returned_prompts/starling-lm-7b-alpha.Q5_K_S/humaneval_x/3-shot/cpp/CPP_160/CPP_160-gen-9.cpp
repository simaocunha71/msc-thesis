    int i,j;
    int oper_size=operato.size();
    int oper_num=operand.size();
    int result=operand[0];
    for (i=0;i<oper_size;i++)
    {
        if (operato[i]=="+")
        result+=operand[i+1];
        if (operato[i]=="-")
        result-=operand[i+1];
        if (operato[i]=="*")
        result*=operand[i+1];
        if (operato[i]=="//")
        result/=operand[i+1];
        if (operato[i]=="**")
        result=pow(result, operand[i+1]);
    }

    return result;
}



