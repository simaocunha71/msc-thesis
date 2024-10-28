    int i,j,k;
    int result;
    for (i=0;i<operato.size();i++)
    {
        if (operato[i]=="+")
        {
            j=i+1;
            result=operand[j];
            for (j=i+2;j<operato.size();j++)
            {
                result+=operand[j];
            }
        }
        if (operato[i]=="*")
        {
            j=i+1;
            result=operand[j];
            for (j=i+2;j<operato.size();j++)
            {
                result*=operand[j];
            }
        }
        if (operato[i]=="/")
        {
            j=i+1;
            result=operand[j];
            for (j=i+2;j<operato.size();j++)
            {
                result/=operand[j];
            }
        }
        if (operato[i]=="^")
        {
            j=i+1;
            result=operand[j];
            for (j=i+2;j<operato.size();j++)
            {
                result^=operand[j];
            }
        }
    }
    return result;
}


