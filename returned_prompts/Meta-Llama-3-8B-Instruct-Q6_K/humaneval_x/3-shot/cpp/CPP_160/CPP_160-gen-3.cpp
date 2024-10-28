    int i;
    int result=operand[0];
    for (i=1;i<operand.size();i++)
    {
        if (operato[i-1]=="+" )
        {
            result+=operand[i];
        }
        else if (operato[i-1]=="-")
        {
            result-=operand[i];
        }
        else if (operato[i-1]=="*")
        {
            result*=operand[i];
        }
        else if (operato[i-1]=="//")
        {
            result=static_cast<int>(result/operand[i]);
        }
        else if (operato[i-1]=="**")
        {
            result=pow(result,operand[i]);
        }
    }
    return result;
} 



