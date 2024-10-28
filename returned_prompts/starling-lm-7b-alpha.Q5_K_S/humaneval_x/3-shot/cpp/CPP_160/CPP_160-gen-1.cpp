    int i,j;
    int result=0;
    if (operato.size()!=operand.size()-1)
    {
        return -1;
    }
    for (i=0;i<operato.size();i++)
    {
        int left=operand[i];
        int right=operand[i+1];
        if (i!=operato.size()-1)
        {
            result=do_algebra(operato,operand);
            operand[i+1]=result;
        }
        else
        {
            result=do_algebra(operato,operand);
        }
    }
    return result;
}




