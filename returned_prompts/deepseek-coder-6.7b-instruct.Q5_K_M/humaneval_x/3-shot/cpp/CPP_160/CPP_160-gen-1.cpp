    int result=operand[0];
    for(int i=0;i<operato.size();i++)
    {
        if(operato[i]=="+")
        {
            result+=operand[i+1];
        }
        if(operato[i]=="-")
        {
            result-=operand[i+1];
        }
        if(operato[i]=="*")
        {
            result*=operand[i+1];
        }
        if(operato[i]=="//")
        {
            result/=operand[i+1];
        }
        if(operato[i]=="**")
        {
            result=pow(result,operand[i+1]);
        }
    }
    return result;
}


