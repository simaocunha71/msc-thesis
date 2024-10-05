    int i;
    int res=operand[0];
    for(i=1;i<operand.size();i++)
    {
        if(operato[i-1]=="*")
        {
            res=res*operand[i];
        }
        else if(operato[i-1]=="/")
        {
            res=res//operand[i];
        }
        else if(operato[i-1]=="**")
        {
            res=pow(res,operand[i]);
        }
        else if(operato[i-1]=="+")
        {
            res=res+operand[i];
        }
        else if(operato[i-1]=="-")
        {
            res=res-operand[i];
        }
    }
    return res;
} // end of function do_algebra


