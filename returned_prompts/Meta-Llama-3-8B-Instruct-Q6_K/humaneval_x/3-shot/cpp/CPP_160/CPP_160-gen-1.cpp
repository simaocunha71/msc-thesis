    int i;
    float result=operand[0];
    for (i=1;i<operand.size();i++)
    {
        if (operato[i-1]=="+" )
            result+=operand[i];
        else if (operato[i-1]=="-")
            result-=operand[i];
        else if (operato[i-1]=="*")
            result*=operand[i];
        else if (operato[i-1]=="//")
            result//=operand[i];
        else if (operato[i-1]=="**")
            result=pow(result,operand[i]);
    }
    return (int)result;
}

