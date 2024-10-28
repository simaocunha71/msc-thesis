    int result;
    int i,j,k;
    int temp;
    for (i=0;i<operato.size();i++)
    {
        if (operato[i]=="+")
        {
            temp=operand[i]+operand[i+1];
            operand[i]=temp;
            operand.erase(operand.begin()+i+1);
            operato.erase(operato.begin()+i);
            i=-1;
        }
        if (operato[i]=="-")
        {
            temp=operand[i]-operand[i+1];
            operand[i]=temp;
            operand.erase(operand.begin()+i+1);
            operato.erase(operato.begin()+i);
            i=-1;
        }
        if (operato[i]=="*")
        {
            temp=operand[i]*operand[i+1];
            operand[i]=temp;
            operand.erase(operand.begin()+i+1);
            operato.erase(operato.begin()+i);
            i=-1;
        }
        if (operato[i]=="//")
        {
            temp=operand[i]/operand[i+1];
            operand[i]=temp;
            operand.erase(operand.begin()+i+1);
            operato.erase(operato.begin()+i);
            i=-1;
        }
        if (operato[i]=="**")
        {
            temp=pow(operand[i],operand[i+1]);
            operand[i]=temp;
            operand.erase(operand.begin()+i+1);
            operato.erase(operato.begin()+i);
            i=-1;
        }
    }

    result=operand[0];
    return result;
}


