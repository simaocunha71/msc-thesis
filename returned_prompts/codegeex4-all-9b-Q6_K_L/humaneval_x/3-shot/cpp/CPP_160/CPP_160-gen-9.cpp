    int i;
    int result;
    for (i=0;i<operato.size();i++)
    {
    if (operato[i]=="+")
    result+=operand[i]+operand[i+1];
    if (operato[i]=="-")
    result+=operand[i]-operand[i+1];
    if (operato[i]=="*")
    result+=operand[i]*operand[i+1];
    if (operato[i]=="//")
    result+=operand[i]/operand[i+1];
    if (operato[i]=="**")
    result+=pow(operand[i],operand[i+1]);
    }
    return result;
}

