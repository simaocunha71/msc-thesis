    int i,j;
    for(i=0;i<operato.size();i++)
    {
        if(operato[i]=="+")
        {
            operand[i+1]=operand[i]+operand[i+1];
        }
        else if(operato[i]=="-")
        {
            operand[i+1]=operand[i]-operand[i+1];
        }
        else if(operato[i]=="*")
        {
            operand[i+1]=operand[i]*operand[i+1];
        }
        else if(operato[i]=="//")
        {
            operand[i+1]=operand[i]/operand[i+1];
        }
        else if(operato[i]=="**")
        {
            operand[i+1]=pow(operand[i],operand[i+1]);
        }
    }
    return operand[operand.size()-1];
}

